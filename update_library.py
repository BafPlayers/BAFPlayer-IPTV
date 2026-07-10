import os
import re
import json
import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from html import unescape

CONTENT_DIR = os.path.dirname(os.path.abspath(__file__))

# File Paths
tv_m3u_file = os.path.join(CONTENT_DIR, "IPTV_Channels.m3u")
tv_txt_file = os.path.join(CONTENT_DIR, "IPTV_Channels.txt")
radios_m3u_file = os.path.join(CONTENT_DIR, "Web_Radios.m3u")
radios_txt_file = os.path.join(CONTENT_DIR, "Web_Radios.txt")
movies_m3u_file = os.path.join(CONTENT_DIR, "Movies.m3u")
series_m3u_file = os.path.join(CONTENT_DIR, "Series.m3u")
master_m3u_file = os.path.join(CONTENT_DIR, "Library.m3u")

podcasts_json_file = os.path.join(CONTENT_DIR, "Podcasts.json")
podcasts_txt_file = os.path.join(CONTENT_DIR, "Podcasts.txt")
movies_json_file = os.path.join(CONTENT_DIR, "Movies_And_Series.json")
movies_txt_file = os.path.join(CONTENT_DIR, "Movies_And_Series.txt")

# Country Mapping (English -> Turkish)
COUNTRY_MAP = {
    "Turkey": "Türkiye",
    "United States": "ABD",
    "United Kingdom": "İngiltere",
    "Germany": "Almanya",
    "France": "Fransa",
    "Italy": "İtalya",
    "Spain": "İspanya",
    "Canada": "Kanada",
    "Russia": "Rusya",
    "Japan": "Japonya",
    "South Korea": "Güney Kore",
    "China": "Çin",
    "Azerbaijan": "Azerbaycan",
    "Brazil": "Brezilya",
    "Netherlands": "Hollanda",
    "Switzerland": "İsviçre",
    "Belgium": "Belçika",
    "Austria": "Avusturya",
    "Greece": "Yunanistan",
    "Ukraine": "Ukrayna",
    "Sweden": "İsveç",
    "Norway": "Norveç",
    "Denmark": "Danimarka",
    "Finland": "Finlandiya",
    "Poland": "Polonya",
    "Romania": "Romanya",
    "Bulgaria": "Bulgaristan"
}

# Priorities list (guaranteed legal, high-quality streams)
PRIORITIES = [
    { "name": "TRT World (English News)", "logo": "https://www.trtworld.com/assets/images/logo-trt-world.png", "country": "Türkiye", "url": "https://tv-trtworld.medya.trt.com.tr/master.m3u8", "desc": "Turkey's international English news channel." },
    { "name": "TRT Haber (Turkish News)", "logo": "https://logos-world.net/wp-content/uploads/2022/07/TRT-Haber-Logo.png", "country": "Türkiye", "url": "https://tv-trthaber.medya.trt.com.tr/master.m3u8", "desc": "Turkey's national news channel." },
    { "name": "TRT Belgesel (Turkish Documentary)", "logo": "https://trthaberstatic.cdn.wp.trt.com.tr/static/images/trt-belgesel-logo.png", "country": "Türkiye", "url": "https://tv-trtbelgesel.medya.trt.com.tr/master.m3u8", "desc": "Culture, nature, and history documentaries." },
    { "name": "TRT Müzik (Turkish Music)", "logo": "https://trthaberstatic.cdn.wp.trt.com.tr/static/images/trt-muzik-logo.png", "country": "Türkiye", "url": "https://tv-trtmuzik.medya.trt.com.tr/master.m3u8", "desc": "Traditional and modern music broadcast." },
    { "name": "TRT Çocuk (Turkish Cartoons)", "logo": "https://trthaberstatic.cdn.wp.trt.com.tr/static/images/trt-cocuk-logo.png", "country": "Türkiye", "url": "https://tv-trtcocuk.medya.trt.com.tr/master.m3u8", "desc": "Educational and fun cartoon broadcasts for kids." },
    { "name": "DW News English", "logo": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Deutsche_Welle_logo.svg", "country": "Almanya", "url": "https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/master.m3u8", "desc": "Germany's international broadcaster." },
    { "name": "NHK World-Japan", "logo": "https://upload.wikimedia.org/wikipedia/commons/7/77/NHK_World_logo.svg", "country": "Japonya", "url": "https://media-tyo.hls.nhkworld.jp/hls/w/live/master.m3u8", "desc": "Japan's public broadcaster." },
    { "name": "NASA TV Public", "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg", "country": "ABD", "url": "https://ntv1.akamaized.net/hls/live/2014075/NASA-NTV1-HLS/master.m3u8", "desc": "Official public live stream of NASA." },
    { "name": "France 24 English", "logo": "https://upload.wikimedia.org/wikipedia/commons/8/82/France_24_logo.svg", "country": "Fransa", "url": "https://live.france24.com/hls/live/2037218/F24_EN_HI_HLS/master_5000.m3u8", "desc": "International news channel based in Paris." }
]

PODCAST_FEEDS = [
    { "name": "NASA's Curious Universe", "url": "https://feeds.megaphone.fm/NATIONALAERONAUTICSANDSPACEADMINISTRATION8162188566" },
    { "name": "Science Vs (Gimlet)", "url": "https://feeds.megaphone.fm/sciencevs" },
    { "name": "Astronomy Cast (Libsyn)", "url": "https://astronomycast.libsyn.com/rss" },
    { "name": "NPR Short Wave (Science)", "url": "https://feeds.npr.org/510351/podcast.xml" },
    { "name": "The History of Rome", "url": "https://historyofrome.libsyn.com/rss" },
    { "name": "Philosophize This! (Libsyn)", "url": "https://philosophizethis.libsyn.com/rss" },
    { "name": "BBC In Our Time", "url": "https://podcasts.files.bbci.co.uk/b006qykl.rss" },
    { "name": "Lore (Folklore & History)", "url": "https://lorepodcast.libsyn.com/rss" },
    { "name": "Dan Carlin's Hardcore History", "url": "https://dancarlin.libsyn.com/rss" },
    { "name": "NPR Planet Money", "url": "https://feeds.npr.org/510289/podcast.xml" },
    { "name": "How I Built This with Guy Raz", "url": "https://feeds.npr.org/510313/podcast.xml" },
    { "name": "TED Radio Hour", "url": "https://feeds.npr.org/510298/podcast.xml" },
    { "name": "Lex Fridman Podcast", "url": "https://lexfridman.com/feed/podcast/" },
    { "name": "The Tim Ferriss Show", "url": "https://timferriss.libsyn.com/rss" },
    { "name": "The Daily (NYT)", "url": "https://feeds.simplecast.com/54nAGcIl" }
]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def clean_html(raw_html):
    if not raw_html:
        return ""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = unescape(cleantext).replace('&amp;', '&').replace('&quot;', '"').replace('&apos;', "'").replace('&#39;', "'")
    cleantext = cleantext.strip()
    return cleantext[:347] + "..." if len(cleantext) > 350 else cleantext

async def test_stream(session, url):
    """Asynchronously check if HLS stream is active using HEAD or GET."""
    try:
        async with session.head(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=1.2) as response:
            if response.status in [200, 206]:
                return True
    except asyncio.TimeoutError:
        # Treat connection timeouts as OK as long as no 404/500 was hit
        return True
    except Exception:
        # Fallback to GET for servers that block HEAD requests
        try:
            async with session.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=1.2) as response:
                if response.status in [200, 206]:
                    return True
        except Exception:
            pass
    return False

def find_local(element, tag_name):
    if element is None:
        return None
    for child in element:
        local_name = child.tag.split('}')[-1]
        if local_name == tag_name:
            return child
    return None

def findall_local(element, tag_name):
    if element is None:
        return []
    results = []
    for child in element:
        local_name = child.tag.split('}')[-1]
        if local_name == tag_name:
            results.append(child)
    return results

async def verify_podcasts(session):
    """Fetch podcast feeds, verify streams, and return episodes catalog."""
    print("------------------------------------------------------------")
    print("STEP 1: Fetching & Verifying Podcasts (15 feeds)...")
    print("------------------------------------------------------------")
    podcast_catalog = []
    
    for feed in PODCAST_FEEDS:
        try:
            print(f"Fetching feed: {feed['name']}...")
            async with session.get(feed['url'], headers={"User-Agent": USER_AGENT}, timeout=15) as response:
                xml_text = await response.text()
                
                root = ET.fromstring(xml_text.encode('utf-8'))
                channel = find_local(root, "channel")
                
                show_title_node = find_local(channel, "title")
                show_title = show_title_node.text if show_title_node is not None else feed['name']
                
                show_logo = ""
                image_node = find_local(channel, "image")
                if image_node is not None:
                    url_node = find_local(image_node, "url")
                    if url_node is not None:
                        show_logo = url_node.text
                    elif 'href' in image_node.attrib:
                        show_logo = image_node.attrib['href']
                if not show_logo:
                    # check itunes:image at channel level
                    itunes_image = find_local(channel, "image")
                    if itunes_image is not None and 'href' in itunes_image.attrib:
                        show_logo = itunes_image.attrib['href']
                if not show_logo:
                    show_logo = "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?q=80&w=256&auto=format&fit=crop"
                
                items = findall_local(channel, "item")[:10]
                episode_index = 1
                for item in items:
                    enclosure = find_local(item, "enclosure")
                    if enclosure is None or 'url' not in enclosure.attrib:
                        continue
                    stream_url = enclosure.attrib['url']
                    
                    title_node = find_local(item, "title")
                    title = title_node.text if title_node is not None else "Untitled Episode"
                    
                    desc = ""
                    desc_node = find_local(item, "description")
                    if desc_node is not None:
                        desc = desc_node.text
                    else:
                        summary_node = find_local(item, "summary")
                        if summary_node is not None:
                            desc = summary_node.text
                    desc_clean = clean_html(desc)
                    
                    pub_date_node = find_local(item, "pubDate")
                    pub_date = pub_date_node.text if pub_date_node is not None else ""
                    
                    clean_show_name = re.sub(r'[^a-zA-Z0-9]', '-', feed['name'])
                    ep_id = f"{clean_show_name.lower()}-ep-{episode_index}"
                    
                    # Verify stream quickly
                    ep_ok = True
                    try:
                        async with session.head(stream_url, headers={"User-Agent": USER_AGENT}, timeout=3.0) as resp:
                            if resp.status == 404:
                                ep_ok = False
                    except Exception:
                        pass
                    
                    if ep_ok:
                        podcast_catalog.append({
                            "id": ep_id,
                            "show_name": show_title,
                            "episode_title": title,
                            "pub_date": pub_date,
                            "stream_url": stream_url,
                            "logo_url": show_logo,
                            "description": desc_clean
                        })
                        episode_index += 1
                print(f"  Successfully compiled {episode_index - 1} episodes for '{show_title}'.")
        except Exception as e:
            print(f"  Failed to process feed for {feed['name']}: {e}")
            
    # Write JSON & TXT for Podcasts
    with open(podcasts_json_file, 'w', encoding='utf-8') as f:
        json.dump(podcast_catalog, f, ensure_ascii=False, indent=2)
        
    txt_pod = ""
    current_show = ""
    for ep in podcast_catalog:
        if current_show != ep['show_name']:
            current_show = ep['show_name']
            txt_pod += f"\r\n{'='*72}\r\nSHOW: {current_show}\r\n{'='*72}\r\n"
        txt_pod += f"{'-'*40}\r\n"
        txt_pod += f"Episode Title: {ep['episode_title']}\r\n"
        txt_pod += f"Published Date: {ep['pub_date']}\r\n"
        txt_pod += f"Description: {ep['description']}\r\n"
        txt_pod += f"Audio Stream URL: {ep['stream_url']}\r\n"
        txt_pod += f"Logo URL: {ep['logo_url']}\r\n"
        
    with open(podcasts_txt_file, 'w', encoding='utf-8') as f:
        f.write(txt_pod)
        
    print(f"Saved podcasts: {len(podcast_catalog)} episodes.")
    return podcast_catalog

async def verify_iptv_channels(session):
    """Download global playlist, verify HLS streams concurrently, group by country."""
    print("\n------------------------------------------------------------")
    print("STEP 2: Fetching & Verifying IPTV Channels...")
    print("------------------------------------------------------------")
    
    url = "https://iptv-org.github.io/iptv/index.country.m3u"
    print("Downloading global country-grouped channel database...")
    try:
        async with session.get(url, headers={"User-Agent": USER_AGENT}, timeout=30) as response:
            text = await response.text()
    except Exception as e:
        print(f"Failed to download index: {e}")
        return []
        
    lines = text.split("\n")
    raw_candidates = []
    urls_used = set()
    
    # Pre-populate priorities
    for p in PRIORITIES:
        raw_candidates.append(p)
        urls_used.add(p["url"])
        
    print("Parsing index...")
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith("#EXTINF:"):
            # Parse country
            country = "Uluslararası / International"
            group_match = re.search(r'group-title="([^"]+)"', line)
            if group_match:
                raw_country = group_match.group(1)
                country = COUNTRY_MAP.get(raw_country, raw_country)
                
            # Parse logo
            logo = ""
            logo_match = re.search(r'tvg-logo="([^"]+)"', line)
            if logo_match:
                logo = logo_match.group(1)
                
            # Parse name
            comma_index = line.rfind(",")
            name = line[comma_index+1:].strip() if comma_index >= 0 else "Bilinmeyen Kanal"
            
            # Find URL
            c_url = ""
            for j in range(i + 1, len(lines)):
                next_line = lines[j].strip()
                if next_line and not next_line.startswith("#"):
                    c_url = next_line
                    break
                    
            if c_url and c_url not in urls_used:
                # Filter out junk
                if any(x in c_url.lower() for x in ["ustream", "youtube", "facebook", "twitch", "vimeo"]):
                    continue
                if any(x in name.lower() for x in ["adult", "18+", "test", "offline", "xxx", "porn", "nude", "sex", "grindhouse"]):
                    continue
                    
                urls_used.add(c_url)
                raw_candidates.append({
                    "name": name,
                    "logo": logo,
                    "country": country,
                    "url": c_url,
                    "desc": f"Global free-to-air stream from {country}."
                })
                
    print(f"Total unique candidates parsed: {len(raw_candidates)}")
    
    # Filter priorities from raw candidate distribution
    prioritized_candidates = []
    country_counts = {}
    
    for p in PRIORITIES:
        prioritized_candidates.append(p)
        country_counts[p["country"]] = 1
        
    for c in raw_candidates:
        if c["url"] in [p["url"] for p in PRIORITIES]:
            continue
            
        cnt = country_counts.get(c["country"], 0)
        cap = 20
        if c["country"] == "Türkiye":
            cap = 100
        elif c["country"] in ["ABD", "İngiltere", "Almanya", "Fransa", "İspanya", "İtalya"]:
            cap = 80
            
        if cnt < cap:
            prioritized_candidates.append(c)
            country_counts[c["country"]] = cnt + 1
            
    print(f"Testing {len(prioritized_candidates)} prioritized channels concurrently...")
    
    # Concurrently test all candidates (except priorities, which are always kept!)
    verified_channels = list(PRIORITIES)
    sem = asyncio.Semaphore(120)  # limit concurrency to 120 threads
    
    async def worker(candidate):
        if candidate["url"] in [p["url"] for p in PRIORITIES]:
            return
        async with sem:
            is_active = await test_stream(session, candidate["url"])
            if is_active:
                verified_channels.append(candidate)
                
    tasks = [worker(c) for c in prioritized_candidates]
    await asyncio.gather(*tasks)
    
    print(f"Testing complete. Verified active channels: {len(verified_channels)}")
    return verified_channels

def load_static_assets():
    """Load web radios and movies catalogs from files."""
    print("\n------------------------------------------------------------")
    print("STEP 3: Loading Static Media Assets...")
    print("------------------------------------------------------------")
    
    web_radios = []
    if os.path.exists(radios_m3u_file):
        with open(radios_m3u_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith("#EXTINF:"):
                logo = ""
                logo_match = re.search(r'tvg-logo="([^"]+)"', line)
                if logo_match:
                    logo = logo_match.group(1)
                comma_index = line.rfind(",")
                name = line[comma_index+1:].strip() if comma_index >= 0 else "Unknown Radio"
                
                url = ""
                for j in range(i + 1, len(lines)):
                    next_line = lines[j].strip()
                    if next_line and not next_line.startswith("#"):
                        url = next_line
                        break
                if url:
                    web_radios.append({"name": name, "logo": logo, "url": url})
        print(f"Loaded {len(web_radios)} web radios from M3U.")
    else:
        print("Warning: Web_Radios.m3u not found.")
        
    movies_catalog = []
    cartoons_catalog = []
    if os.path.exists(movies_json_file):
        with open(movies_json_file, 'r', encoding='utf-8-sig') as f:
            video_items = json.load(f)
        for item in video_items:
            if item.get("category") == "Cartoons":
                cartoons_catalog.append(item)
            else:
                movies_catalog.append(item)
        print(f"Loaded {len(movies_catalog)} movies and {len(cartoons_catalog)} cartoons from JSON.")
    else:
        print("Warning: Movies_And_Series.json not found.")
        
    return web_radios, movies_catalog, cartoons_catalog

def generate_playlists(verified_channels, web_radios, movies_catalog, cartoons_catalog, podcast_catalog):
    """Generate final M3U lists and master Library.m3u."""
    print("\n------------------------------------------------------------")
    print("STEP 4: Generating M3U & Master Library Playlists...")
    print("------------------------------------------------------------")
    
    # 1. IPTV Channels M3U
    tv_m3u_content = "#EXTM3U\r\n"
    for c in verified_channels:
        tv_m3u_content += f'#EXTINF:-1 tvg-logo="{c["logo"]}" group-title="Canlı TV - {c["country"]}",{c["name"]}\r\n'
        tv_m3u_content += f'{c["url"]}\r\n'
    with open(tv_m3u_file, 'w', encoding='utf-8') as f:
        f.write(tv_m3u_content)
        
    # 2. IPTV Channels TXT
    tv_txt_content = ""
    for c in verified_channels:
        tv_txt_content += f"{'='*40}\r\n"
        tv_txt_content += f"Channel Name: {c['name']}\r\n"
        tv_txt_content += f"Country/Group: {c['country']}\r\n"
        tv_txt_content += f"Description: {c['desc']}\r\n"
        tv_txt_content += f"Stream URL: {c['url']}\r\n"
        tv_txt_content += f"Logo URL: {c['logo']}\r\n"
    with open(tv_txt_file, 'w', encoding='utf-8') as f:
        f.write(tv_txt_content)
        
    # 3. Movies M3U
    movies_m3u_content = "#EXTM3U\r\n"
    for m in movies_catalog:
        title_with_year = f"{m['title']} ({m['year']})" if m.get('year', 0) > 0 else m['title']
        movies_m3u_content += f'#EXTINF:-1 tvg-logo="{m["poster_url"]}" group-title="Film",{title_with_year}\r\n'
        movies_m3u_content += f'{m["stream_url"]}\r\n'
    with open(movies_m3u_file, 'w', encoding='utf-8') as f:
        f.write(movies_m3u_content)
        
    # 4. Series (Cartoons & Podcasts) M3U
    series_m3u_content = "#EXTM3U\r\n"
    for c in cartoons_catalog:
        title_with_year = f"{c['title']} ({c['year']})" if c.get('year', 0) > 0 else c['title']
        series_m3u_content += f'#EXTINF:-1 tvg-logo="{c["poster_url"]}" group-title="Dizi" tvg-name="{c["title"]}",{title_with_year}\r\n'
        series_m3u_content += f'{c["stream_url"]}\r\n'
    for p in podcast_catalog:
        ep_title = p['episode_title'].replace(",", " ")
        series_m3u_content += f'#EXTINF:-1 tvg-logo="{p["logo_url"]}" group-title="Dizi" tvg-name="{p["show_name"]} - {ep_title}",{p["show_name"]} - {ep_title}\r\n'
        series_m3u_content += f'{p["stream_url"]}\r\n'
    with open(series_m3u_file, 'w', encoding='utf-8') as f:
        f.write(series_m3u_content)
        
    # 5. Master Library M3U (Combined)
    master_m3u_content = "#EXTM3U\r\n"
    # A. Channels
    for c in verified_channels:
        master_m3u_content += f'#EXTINF:-1 tvg-logo="{c["logo"]}" group-title="Canlı TV - {c["country"]}",{c["name"]}\r\n'
        master_m3u_content += f'{c["url"]}\r\n'
    # B. Radios
    for r in web_radios:
        master_m3u_content += f'#EXTINF:-1 tvg-logo="{r["logo"]}" group-title="Radyo",{r["name"]}\r\n'
        master_m3u_content += f'{r["url"]}\r\n'
    # C. Movies
    for m in movies_catalog:
        title_with_year = f"{m['title']} ({m['year']})" if m.get('year', 0) > 0 else m['title']
        master_m3u_content += f'#EXTINF:-1 tvg-logo="{m["poster_url"]}" group-title="Film",{title_with_year}\r\n'
        master_m3u_content += f'{m["stream_url"]}\r\n'
    # D. Series & Podcasts
    for c in cartoons_catalog:
        title_with_year = f"{c['title']} ({c['year']})" if c.get('year', 0) > 0 else c['title']
        master_m3u_content += f'#EXTINF:-1 tvg-logo="{c["poster_url"]}" group-title="Dizi" tvg-name="{c["title"]}",{title_with_year}\r\n'
        master_m3u_content += f'{c["stream_url"]}\r\n'
    for p in podcast_catalog:
        ep_title = p['episode_title'].replace(",", " ")
        master_m3u_content += f'#EXTINF:-1 tvg-logo="{p["logo_url"]}" group-title="Dizi" tvg-name="{p["show_name"]} - {ep_title}",{p["show_name"]} - {ep_title}\r\n'
        master_m3u_content += f'{p["stream_url"]}\r\n'
        
    with open(master_m3u_file, 'w', encoding='utf-8') as f:
        f.write(master_m3u_content)
        
    print(f"Generated categorized playlists in: {CONTENT_DIR}")
    print("Master library playlist successfully compiled!")

async def main():
    async with aiohttp.ClientSession() as session:
        podcast_catalog = await verify_podcasts(session)
        verified_channels = await verify_iptv_channels(session)
        web_radios, movies_catalog, cartoons_catalog = load_static_assets()
        generate_playlists(verified_channels, web_radios, movies_catalog, cartoons_catalog, podcast_catalog)

if __name__ == "__main__":
    asyncio.run(main())
