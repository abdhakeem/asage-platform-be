import random


class Engine:
    def __init__(self):
        self.calc_methods = ["Supplier-specific", "Average-data", "Hybrid"]
        self.ef_source = ["IPCC", "UK DEFRA", "US EPA", "ECOINVENT", "GHG PROTOCOL"]
        self.emission_factor = {"bauxite": 100}

    def process(self, extracted_info):
        for info in extracted_info["materials"]:
            # calc method derivation and EF source is outside the scope of the hackathon, return random choice for
            # now as derivation logic is confidential
            info["calc_method"] = random.choice(self.calc_methods)
            info["ef_source"] = random.choice(self.ef_source)
            # dummy calculation logic in MVP as derivation is outside the scope of this hackathon
            if info["item"].lower() in self.emission_factor:
                ef = self.emission_factor[info["item"].lower()]
            else:
                ef = 0
            info["emissions"] = ef * info["quantity"]
        return extracted_info
