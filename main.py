import requests
from json import loads
import os
import threading
import customtkinter as ctk
from webbrowser import open as webopen
from CTkMessagebox import CTkMessagebox
import subprocess

# Credits to my goat the Big L hes so tuff, thanks for the idea this is heavily inspired but you cant really change that much. I only know ctk as a gui library :sob:

def main():
    app = ctk.CTk()
    app.geometry("1120x620") 
    app.title("Config Creator") 
    app.resizable(False, False) 
    
    
    
    Version = 1.0
    UpdBtn = ctk.CTkButton(app, text=f"Update\n{Version}", font=ctk.CTkFont(size=14, weight="bold"), command=lambda: subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "Update.ps1"]))
    UpdBtn.place(x=425, y=530)
    
    Gamemodes = ["None", "BossRush", "Bounty", "Challenge", "Custom", "Default", "Dungeon", "Event", "Infinite", "LegendStage", "Odyseey", "Portal", "Raid", "Rift", "Story", "Worldline"]
    MapBossRush = ["Blood_Red_Chamber", "Dark_Tainted_Tyrant", "Shibuya_Aftermath", "Rumbling_Event"]
    MapBountyChallange = ["Burning_Spirit_Tree", "Crystal_Chapel", "Double_Dungeon", "Downtown_Tokyo", "Edge_of_Heaven", "Frozen_Port", "Golden_Castle", "Hill_of_Swords", "Imprisoned_Island", "Kuinshi_Palace", "Lebereo_Raid", "Martial_Island", "Planet_Namek", "Sand_Village", "Shibuya_Aftermath", "Shibuya_Station", "Shining_Castle", "Spirit_Society", "The_Land_of_Gods", "Tokyo_Railway", "Underground_Church"]
    MapCustom = ["Blood_Red_Chamber", "Burning_Spirit_Tree", "Crystal_Chapel", "Dark_Tainted_Tyrant", "Double_Dungeon", "Downtown_Tokyo", "Dried_Lake", "Edge_of_Heaven", "Frozen_Port", "Frozen_Volcano", "Golden_Castle", "HAPPY_Factory", "Hill_of_Swords", "Imprisoned_Island", "Jeju_Island", "Jojo", "Jojo_2", "Kuinshi_Palace", "Lebereo_Raid", "Lich_Kings_Throne", "Martial_Island", "Mountain_Shrine", "Old_Lobby", "Old_Namek", "Planet_Namek", "Planet_Namek_Spring", "Ruined_City", "Rumbling_Event", "Sand_Village", "Shibuya_Aftermath", "Blood_Red_Chamber", "Burning_Spirit_Tree", "Crystal_Chapel", "Dark_Tainted_Tyrant", "Double_Dungeon", "Downtown_Tokyo", "Dried_Lake", "Edge_of_Heaven", "Frozen_Port", "Frozen_Volcano", "Golden_Castle", "HAPPY_Factory", "Hill_of_Swords", "Imprisoned_Island", "Jeju_Island", "Jojo", "Jojo_2", "Kuinshi_Palace", "Lebereo_Raid", "Lich_Kings_Throne", "Martial_Island", "Mountain_Shrine", "Old_Lobby", "Old_Namek", "Planet_Namek", "Planet_Namek_Spring", "Ruined_City", "Rumbling_Event", "Sand_Village", "Shibuya_Aftermath",
    "Shibuya_Aftermath", "Shibuya_Station", "Shining_Castle", "Spider_Forest", "Spirit_Society", "Sun_Temple", "The_Land_of_Gods", "Tokyo_Railway", "Underground_Church", "Underworld", "Winter_Bleach", "Winter_Bleach_Regular"]
    MapAll = ["All", "Blood_Red_Chamber", "Burning_Spirit_Tree", "Crystal_Chapel", "Dark_Tainted_Tyrant", "Double_Dungeon", "Downtown_Tokyo", "Dried_Lake", "Edge_of_Heaven", "Frozen_Port", "Frozen_Volcano", "Golden_Castle", "HAPPY_Factory", "Hill_of_Swords", "Imprisoned_Island", "Jeju_Island", "Jojo", "Jojo_2", "Kuinshi_Palace", "Lebereo_Raid", "Lich_Kings_Throne", "Martial_Island", "Mountain_Shrine", "Old_Lobby", "Old_Namek", "Planet_Namek", "Planet_Namek_Spring", "Ruined_City", "Rumbling_Event", "Sand_Village", "Shibuya_Aftermath", "Blood_Red_Chamber", "Burning_Spirit_Tree", "Crystal_Chapel", "Dark_Tainted_Tyrant", "Double_Dungeon", "Downtown_Tokyo", "Dried_Lake", "Edge_of_Heaven", "Frozen_Port", "Frozen_Volcano", "Golden_Castle", "HAPPY_Factory", "Hill_of_Swords", "Imprisoned_Island", "Jeju_Island", "Jojo", "Jojo_2", "Kuinshi_Palace", "Lebereo_Raid", "Lich_Kings_Throne", "Martial_Island", "Mountain_Shrine", "Old_Lobby", "Old_Namek", "Planet_Namek", "Planet_Namek_Spring", "Ruined_City", "Rumbling_Event", "Sand_Village", "Shibuya_Aftermath",
    "Shibuya_Aftermath", "Shibuya_Station", "Shining_Castle", "Spider_Forest", "Spirit_Society", "Sun_Temple", "The_Land_of_Gods", "Tokyo_Railway", "Underground_Church", "Underworld", "Winter_Bleach", "Winter_Bleach_Regular"]
    MapDungeon = ["Frozen_Volcano", "Jeju_Island", "Underworld"]
    MapEvent = ["Double_Dungeon", "Golden_Castle", "Kuinshi_Palace", "The_Land_of_Gods", "Shining_Castle", "Crystal_Chapel", "Burning_Spirit_Tree", "Old_Lobby", "Old_Namek", "Frozen_Port", "Lich_Kings_Throne", "Winter_Bleach"]
    MapInf = ["Double_Dungeon", "Edge_of_Heaven", "Frozen_Port", "Hill_of_Swords", "Lebereo_Raid", "Lich_Kings_Throne", "Martial_Island", "Planet_Namek", "Sand_Village", "Shibuya_Station", "Spirit_Society", "Underground_Church", "Winter_Bleach"]
    MapLegendStage = ["Burning_Spirit_Tree", "Crystal_Chapel", "Double_Dungeon", "Golden_Castle", "Imprisoned_Island", "Kuinshi_Palace", "Sand_Village", "Shibuya_Aftermath", "Shining_Castle", "The_Land_of_Gods", "Tokyo_Railway"]
    MapOdyseey = ["Double_Dungeon", "Planet_Namek", "Sand_Village", "Shibuya_Aftermath", "Shibuya_Station"]
    MapPortal = ["Lich_Kings_Throne"]
    MapRaid = ["HAPPY_Factory", "Jojo", "Jojo_2", "Ruined_City", "Spider_Forest"]
    MapRift = ["Imprisoned_Island", "Kuinshi_Palace", "Mountain_Shrine", "Underground_Church"]
    MapStory = ["Double_Dungeon", "Downtown_Tokyo", "Edge_of_Heaven", "Frozen_Port", "Hill_of_Swords", "Lebereo_Raid", "Martial_Island", "Planet_Namek", "Sand_Village", "Shibuya_Station", "Spirit_Society", "Underground_Church"]
    
    GameModeOpt = ctk.CTkOptionMenu(app, width=200, height=45, values=Gamemodes)
    GameModeOpt.place(x=505, y=400)

    MapOpt = ctk.CTkOptionMenu(app, values=["None"])
    MapOpt.place(x=535, y=465)

    def on_change(selected=None):
        if selected is None:
            selected = GameModeOpt.get()
        match selected:
            case "None": MapOpt.configure(values=["None"])
            case "Boss Rush": MapOpt.configure(values=MapBossRush)
            case "Bounty": MapOpt.configure(values=MapBountyChallange)
            case "Challenge": MapOpt.configure(values=MapBountyChallange)
            case "Custom": MapOpt.configure(values=MapCustom)
            case "Default": MapOpt.configure(values=MapAll)
            case "Dungeon": MapOpt.configure(values=MapDungeon)
            case "Event": MapOpt.configure(values=MapEvent)
            case "Infinite": MapOpt.configure(values=MapInf)
            case "Legend Stage": MapOpt.configure(values=MapLegendStage)
            case "Odyssey": MapOpt.configure(values=MapOdyseey)
            case "Portal": MapOpt.configure(values=MapPortal)
            case "Raid": MapOpt.configure(values=MapRaid)
            case "Rift": MapOpt.configure(values=MapRift)
            case "Story": MapOpt.configure(values=MapStory)
            
        MapOpt.set("None")

    GameModeOpt.configure(command=on_change)


    ctk.CTkLabel(app, text="Output", font=ctk.CTkFont(size=14, weight="bold")).place(x=25, y=10) 
    output_txt = ctk.CTkTextbox(app, width=220, height=480, state="disabled")
    output_txt.place(x=25, y=40)
    
    def save():
        Gamemode = GameModeOpt.get()
        Map = MapOpt.get()
        try:
            with open(f"Data/Config/{Gamemode}/{Map}/{Map}_Strategy.txt", "w") as w:
                text = output_txt.get("1.0", "end-1c")
                w.write(text)
        except FileNotFoundError: # these will create the folders if they dont exist
            os.makedirs(f"Data/Config/{Gamemode}", exist_ok=True)
            os.makedirs(f"Data/Config/{Gamemode}/{Map}", exist_ok=True)
            with open(f"Data/Config/{Gamemode}/{Map}/{Map}_Strategy.txt", "w") as w:
                text = output_txt.get("1.0", "end-1c")
                w.write(text)
            
    SaveBtn = ctk.CTkButton(app, text="Save", font=ctk.CTkFont(size=14, weight="bold"), command=save)
    SaveBtn.place(x=60, y=540)
            
    ctk.CTkLabel(app, text="Prompt", font=ctk.CTkFont(size=14, weight="bold")).place(x=290, y=10)
    prompt_txt = ctk.CTkTextbox(app, width=380, height=180)
    prompt_txt.place(x=265, y=40)

    ctk.CTkLabel(app, text="Slot Context  (optional)", font=ctk.CTkFont(size=12, weight="bold")).place(x=265, y=235)
    slot_entries: dict[str, ctk.CTkEntry] = {}
    col_x = [265, 475]   
    entry_width = 150   
    label_width = 55     
    for i in range(1, 7):
        col = (i - 1) % 2
        row = (i - 1) // 2
        x, y = col_x[col], 265 + row * 45
        ctk.CTkLabel(app, text=f"Slot {i}:").place(x=x, y=y)
        entry = ctk.CTkEntry(app, width=entry_width, placeholder_text="unit name")
        entry.place(x=x + label_width, y=y)
        slot_entries[f"Slot {i}"] = entry

    
    def _show_output(text: str) -> None:
        output_txt.configure(state="normal")
        output_txt.delete("0.0", "end")
        output_txt.insert("0.0", text)
        output_txt.configure(state="disabled")

    def _show_error(msg: str) -> None:
        error_txt.configure(state="normal")
        error_txt.delete("0.0", "end")
        error_txt.insert("0.0", msg)
        error_txt.configure(state="disabled")

    def _clear_error() -> None:
        error_txt.configure(state="normal")
        error_txt.delete("0.0", "end")
        error_txt.configure(state="disabled")


    def send() -> None:
        api_key = api_key_entry.get().strip()
        if not api_key:
            CTkMessagebox(title="No API Key", message="Please enter or load your API Key.")
            return

        describe_config = prompt_txt.get("0.0", "end").strip()
        if not describe_config:
            CTkMessagebox(title="Empty Prompt", message="Please enter a prompt first.")
            return

        
        filled_slots = {k: v.get().strip() 
                        for k, v in slot_entries.items() 
                        if v.get().strip()}
        slots_str = str(filled_slots) if filled_slots else "No slot context provided."

        try:
            with open("prompt.txt", "r", encoding="utf-8") as f:
                system_prompt = f.read()
        except FileNotFoundError:
            system_prompt = "You are a config creator assistant."

        send_btn.configure(state="disabled", text="Sending…")
        _show_output("Waiting for response…")
        _clear_error()

        def api_call() -> None:
            try:
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Accept": "application/vnd.github+json",
                    "X-GitHub-Api-Version": "2022-11-28",
                    "Content-Type": "application/json",
                }
                payload = {
                    "model": "openai/GPT-4.1",
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                system_prompt
                                + '\n on the predefined slots if the prompt says "Alocard" instead of "Slot 1" and the Slot 1 value is Alocard you use Slot 1 in the output '
                                  "the value assigned to it:\n"
                                + slots_str
                            ),
                        },
                        {"role": "user", "content": describe_config},
                    ],
                }
                r = requests.post(
                    "https://models.github.ai/inference/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=60,
                )
                data = loads(r.content.decode("utf-8"))

                if "error" in data:
                    raise RuntimeError(data["error"].get("message", str(data["error"])))

                text = data["choices"][0]["message"]["content"]
                app.after(0, lambda: _show_output(text))
                app.after(0, _clear_error)

            except Exception as exc:
                app.after(0, lambda e=exc: _show_error(str(e)))
            finally:
                app.after(0, lambda: send_btn.configure(state="normal", text="Send Prompt"))

        threading.Thread(target=api_call, daemon=True).start()

    send_btn = ctk.CTkButton(app, text="Send Prompt", width=200, height=45, command=send)
    send_btn.place(x=290, y=400)

    ctk.CTkButton(
        app, text="Get API Key", width=150, height=35,
        command=lambda: webopen("https://github.com/marketplace/models/azure-openai/gpt-4-1"),
    ).place(x=315, y=460)

    ctk.CTkLabel(app, text="API Key", font=ctk.CTkFont(size=14, weight="bold")).place(x=800, y=10)
    api_key_entry = ctk.CTkEntry(app, width=280, height=38, show="*", placeholder_text="Paste GitHub token…")
    api_key_entry.place(x=780, y=40)

    def load_key() -> None:
        if os.path.exists("key.txt"):
            with open("key.txt", "r") as f:
                key = f.read().strip()
            api_key_entry.delete(0, "end")
            api_key_entry.insert(0, key)
        else:
            CTkMessagebox(
                title="API Key not found",
                message='No key.txt found.\nPaste your key above or press "Get API Key".',
            )

    def save_key() -> None:
        key = api_key_entry.get().strip()
        if not key:
            CTkMessagebox(title="Error", message="Nothing to save — enter a key first.")
            return
        with open("key.txt", "w") as f:
            f.write(key)
        CTkMessagebox(title="Saved", message="API Key saved to key.txt.")

    load_key() 

    ctk.CTkButton(app, text="Load from file", width=130, height=32, command=load_key).place(x=780, y=90)
    ctk.CTkButton(app, text="Save to file",   width=130, height=32, command=save_key).place(x=920, y=90)

    ctk.CTkLabel(app, text="Errors", font=ctk.CTkFont(size=14, weight="bold")).place(x=800, y=135)
    error_txt = ctk.CTkTextbox(app, width=280, height=380, state="disabled")
    error_txt.place(x=780, y=165)

    on_change()

    app.mainloop()


if __name__ == "__main__":
    main()