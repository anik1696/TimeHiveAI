# nodes.py
# TimeHive AI - Node definitions

import requests
from datetime import datetime
from zoneinfo import ZoneInfo
from tzfpy import get_tz


def parse_node(state: dict) -> dict:
    query = state.get("query", "").strip()
    return {"city": query}


def geocode_node(state: dict) -> dict:
    city = state.get("city", "")

    if not city:
        return {"error": "City name missing!"}

    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    headers = {"User-Agent": "TimeHiveAI/1.0"}

    res = requests.get(url, params=params, headers=headers, timeout=10)
    data = res.json()

    if not data:
        return {"error": f"Location '{city}' not found!"}

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    name = data[0].get("display_name", city)

    return {"lat": lat, "lon": lon, "name": name}


def timezone_node(state: dict) -> dict:
    if state.get("error"):
        return state

    lat = state.get("lat")
    lon = state.get("lon")

    tz_name = get_tz(lon, lat)

    if not tz_name:
        return {"error": "Failed to detect timezone!"}

    now = datetime.now(ZoneInfo(tz_name))
    offset = now.utcoffset().total_seconds() / 3600

    return {
        "tz_name": tz_name,
        "local_time": now.strftime("%I:%M %p"),
        "date": now.strftime("%A, %B %d, %Y"),
        "abbr": now.strftime("%Z"),
        "offset": offset
    }


def format_node(state: dict) -> dict:
    if state.get("error"):
        return {"reply": state["error"]}

    name = state.get("name", "")

    reply = (
        f"### 🐝 TimeHive AI — Result\n"
        f"**Location:** {name}\n"
        f"**Timezone:** `{state.get('tz_name')}`\n"
        f"**UTC Offset:** `UTC{state.get('offset'):+.1f}`\n"
        f"**Local Time:** **{state.get('local_time')}**\n"
        f"**Date:** {state.get('date')}\n"
        f"**Abbr:** `{state.get('abbr')}`\n"
    )

    return {"reply": reply}
