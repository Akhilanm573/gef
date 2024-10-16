class WasteWatch:
    def __init__(self):
        self.waste_data = {}

    def add_waste(self, category, amount):
        if category in self.waste_data:
            self.waste_data[category] += amount
        else:
            self.waste_data[category] = amount
        print(f"Added {amount} kg of {category} waste.")

    def total_waste(self):
        total = sum(self.waste_data.values())
        print(f"Total waste generated: {total} kg")

    def waste_report(self):
        print("Waste Report:")
        for category, amount in self.waste_data.items():
            print(f"{category}: {amount} kg")

    def reduction_tips(self):
        tips = {
            'Plastic': 'Use reusable bags and bottles.',
            'Food': 'Plan meals to avoid overbuying.',
            'Paper': 'Go digital whenever possible.',
            'Electronics': 'Recycle old devices responsibly.'
        }
        for category, tip in tips.items():
            print(f"{category} tip: {tip}")

if __name__ == "__main__":
    waste_watch = WasteWatch()
    
    # Sample data
    waste_watch.add_waste('Plastic', 2.5)
    waste_watch.add_waste('Food', 1.2)
    waste_watch.add_waste('Paper', 0.8)
    
    waste_watch.total_waste()
    waste_watch.waste_report()
    waste_watch.reduction_tips()
