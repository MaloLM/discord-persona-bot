import asyncio
import json
from random import choice

botPath = "/home/harkinian/scripts/KingBot"

class GBCommon:
    """
    Common functionalities for managing bot data.
    Handles saving, loading, and manipulating persistent data.
    """

    def __init__(self):
        self.data_save = {"cycle_random_select": {}, "chaine_counter": {}}
        self.fsLock = asyncio.Lock()
        self.load()

    def set(self, main, sub, data):
        """
        Sets the data for a specific category and subcategory.
        """
        self.data_save[main][sub] = data
        self.save()

    def get(self, main, sub):
        """
        Retrieves the data for a specific category and subcategory.
        """
        return self.data_save[main].get(sub, None)

    def save(self, file_name=f"{botPath}/conf/saveganonbot.json"):
        """
        Saves the current state of data to a JSON file.
        """
        print(f"Saving in {file_name}...")
        try:
            with open(file_name, "w+") as f:
                json.dump(self.data_save, f)
            print(f"Saved {file_name}!")
        except IOError as e:
            print(f"Error saving file: {e}")

    def load(self, file_name=f"{botPath}/conf/saveganonbot.json"):
        """
        Loads the data from a JSON file.
        """
        print(f"Loading {file_name}...")
        try:
            with open(file_name, "r") as f:
                self.data_save = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading file: {e}")

    def cycle_random_select(self, options, saveSlot):
        """
        Selects an option cyclically from a list, avoiding recent selections.
        """
        nb_options = len(options)
        if nb_options <= 1:
            print(f"cycle_random_select: Not enough options: {options}")
            return options[0]

        used_indexes = self.get("cycle_random_select", saveSlot) or []

        # Determine available indexes
        indexes = [i for i in range(nb_options) if i not in used_indexes]
        chosen_index = choice(indexes)

        # Reset used indexes if all options have been used
        if nb_options <= len(used_indexes) + 1:
            used_indexes = []
        used_indexes.append(chosen_index)

        self.set("cycle_random_select", saveSlot, used_indexes)
        return options[chosen_index]
