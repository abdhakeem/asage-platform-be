import json
import random


def simple_process(item_name):
    raw = item_name.lower().split("(")[0]
    if raw.split(" ")[0] == "aluminium" or raw.split(" ")[0] == "aluminum":
        raw = "aluminium"
    return raw.strip()


class Engine:
    def __init__(self):
        self.calc_methods = ["Supplier-specific", "Average-data", "Hybrid"]
        self.ef_source = ["IPCC", "UK DEFRA", "US EPA", "ECOINVENT", "GHG PROTOCOL"]
        self.emission_factor = json.load(open("data/emission_factors.json"))

    def calculate(self, extracted_info):
        for info in extracted_info["materials"]:
            # calc method derivation and EF source is outside the scope of the hackathon, return random choice for
            # now as derivation logic is confidential
            info["calc_method"] = random.choice(self.calc_methods)
            info["ef_source"] = random.choice(self.ef_source)
            # dummy calculation logic in MVP as derivation is outside the scope of this hackathon
            item_name = simple_process(info["item"])
            if item_name in self.emission_factor:
                info["ef"] = self.emission_factor[item_name]
            else:
                info["ef"] = 0
            info["emissions"] = info["ef"] * info["quantity"]
            if info["ef"] ==0 or info["emissions"] == 0:
                info["emissions"] = None
                info["ef"] = None
        return extracted_info
