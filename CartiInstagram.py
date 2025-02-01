import json
import os
import pandas as pd


INSTAGRAM_FOLDER = "playboicarti/"


posts_data = []

# Loop through all JSON files in the folder
for filename in os.listdir(INSTAGRAM_FOLDER):
    if filename.endswith(".json"):  # Ensure it's a JSON file
        with open(os.path.join(INSTAGRAM_FOLDER, filename), "r", encoding="utf-8") as file:
            data = json.load(file)

            # Extract key details
            caption = data.get("edge_media_to_caption", {}).get("edges", [{}])[0].get("node", {}).get("text", "No caption")
            likes = data.get("edge_media_preview_like", {}).get("count", 0)
            comments = data.get("edge_media_to_parent_comment", {}).get("count", 0)
            timestamp = data.get("taken_at_timestamp", "")

            # Append to list
            posts_data.append([timestamp, caption, likes, comments])


df = pd.DataFrame(posts_data, columns=["Timestamp", "Caption", "Likes", "Comments"])
df.to_csv("CartiInstagram.csv", index=False)
print("✅ Instagram data saved to CartiInstagram.csv")
