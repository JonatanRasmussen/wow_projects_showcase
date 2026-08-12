I created this repository to showcase my various *personal* World of Warcraft project from 2023-2026.


# Raider.io applicant look-up *[Repository link](https://github.com/JonatanRasmussen/raider_io_peaking)*

Scripts to look up and rank every applicant for my WoW dungeon- or raid groups, inspired by the OP.GG website for LoL.

**To get started**, run 'main.py' or open 'websitetest.html' for a nice GUI.

A json of each applicant (generated via the Raider.io addon) is manually copy-pasted into the "input.json" file or GUI window. Then, each player profile will then be looked up using the raider.io API, and my code will then rank/present each player based on their accomplishments from earlier seasons.

Rankings include Player name, Role, Class, missing enchant/gem counter, iLvl, CE/AOTC achievement count, KSM count, Best run, m+ Score, completion timers, recent runs, and Age (time since last run). There is also a score breakdown for each dungeon.

See the below image for an example of what the website looks like.

![Image link](images/riopeek_web_preview.png)

And if run via the terminal, here is what the terminal output looks like.

![Image link](images/riopeek_showcase.PNG)


# Warcraftlog analysis and summary *[Repository link](https://github.com/JonatanRasmussen/raider_io_peaking)*

Scripts to look up every M+ player you've played with throughout a WoW season to see what rank they ended up at. It will also generate a summary of your journey,
providing statistics over how many attempts / groups you needed for each of your M+ keys.

This is not just data visualization, it regex-parses messy data from 100+ logs (captured raw from the browser by manually doing a Ctrl+A Ctrl+C on all visible data). Then, we re-contruct the player's M+ "journey" by cross-referencing upload dates to see how many attempts (logs) were recorded before each dungeon was completed for the first time.

**How to use:**, run 'logrun_rio_integration.py' or 'logrun.py' (to generate a summary with or without end-of-season player scores, respectively).

See this image for a screenshot of what the summary looks like.

![Image link](images/logrun_showcase.png)


# Interface mod: /say Callouts M+ *[Repository link](https://github.com/JonatanRasmussen/world_of_warcraft_mod_mplus_say_callouts_weakaura)*

This is an interface mod that I developed for the WoW community and it ended up becoming quite popular (24.000 views / 1300+ downloads / 220 stars via the wago.io website, and an estimated 10.000+ additional in-game downloads via peer-to-peer WeakAura-sharing.)

It uses event-driven logic to parse the combat log, looking for spell_ids that I considered dangerous for the given M+ season. I manually configured spell casting logic for 100+ new spell_ids for every content patch (twice per year), this included going into each new dungeon and manually recording the spell cast patterns of enemies (channeled/instant casts, duration, frequency, NPC-ID, etc.). To optimize for performance, I configured load-conditions for each dungeon to limit CPU-use.

I did for all 6 major game patches from 2023-2025 (DF season 2-4, TWW season 1-3), **[see my Wago.io page for more details.](https://wago.io/6CDe7U7t6)**.

This project was created via the WeakAura-framework (I used the in-game editor to generate Lua-code, so there's not much code to show here on GitHub). I did however have python code to test and validate the spell casting data I recorded in-game by cross-referencing it with public spell data on the Wowhead website.

*[![(YouTube thumbnail screenshot, click to open on YouTube.)](https://img.youtube.com/vi/JSiVJAfD0WQ/0.jpg)](https://www.youtube.com/watch?v=JSiVJAfD0WQ)*

*(YouTube thumbnail screenshot, click to open video clip on YouTube.)*


# Death statistics scraper *[Repository link](https://github.com/JonatanRasmussen/wow_mythicplus_say)*

Various helper scripts to test and validate spell data for my Interface mod: */say Callouts M+*.

This code served two purposes; first, it would iterate over each row of hand-written spell data in my Excel-spreadsheet to see if the spell data I had recored in-game matched spell data scraped from the wowhead website (it also tried to parse the Lua-code generated via the in-game WeakAura editor to see if the data matched my spreadsheet data, but this was never fully implemented.)

Second, the code was able to fetch all public logs from Warcraftlogs.com for a given dungeon, and it would then for each spell_id record: *A: How often was the spell cast, and B: how often did that spell result in a player death*. This was very important for my design process, as I had to decide which spells should and shouldn't trigger an alert in my interface. Unlike most other mods that did something similar, I put a lot of effort into carefully configuring which spells should trigger an alert; if they were cast too frequently, or if they weren't lethal enough, people would consider the alerts too noisy.

![Image link](images/excel_spell_data_showcase.png)

![Image link](images/deathstats_showcase.png)


# Gear drop optimizer *[Repository link](https://github.com/JonatanRasmussen/world_of_warcraft_stuff)*

This project intended to help players optimize their loot by telling them how likely each type of gear (helmet, gloves, weapon, etc.) was to drop from a given dungeon.

This is quite hard to calculate, as you can only see the full loot table for each boss. But each boss is part of a dungeon with multiple bosses (that you must also kill), and the actual drop chance of each item depends on the size of the loot table, the loot elligibility of your *and your allies* class/spec.

I copied the final output into a massive spreadsheet with multiple drop chance tables for each gear slot and playable class/spec:
[Google spreadsheet link](https://docs.google.com/spreadsheets/d/1HwX7lmcGNRF1X0eqS8Gbttr7EWLi2pE43eD8ctp9D78/edit?gid=12643874#gid=12643874)

**How the code works:** We input a Wowhead-website link to the most recent dungeon pool. From wowhead, we then scrape: each dungeon, each boss for each dungeon, and each piece of loot from each boss. We then parse out the stats for a given piece of loot (str/agi/int and gear type), which then allows us to reverse-construct what every spec in the game can probabilistically expect to have looted after completing a full dungeon run. And if you are missing any combination of gear (chestplate/trinket/necklace, but NOT a helmet/glove/weapon), the script is also smart enough to calculate which dungeon is statistically most likely to provide a loot upgrade.

![Image link](images/wow_lootdrop_optimize_showcase.png)


# Item loot tables *[Repository link](https://github.com/JonatanRasmussen/wow_items_10_1)*

Not all combinations of secondary stats exist for a given gear slot (this changes from season to season). This code scrapes Wowhead to find all available items for a given season, and it then calculates which secondary stat combinations exist in the game for each gear slot. A year later, this project turned into "Gear drop optimizer" which is a similar but much larger project hosted in a separate repository.

![Image link](images/wow_item_secondaries_showcase.png)
