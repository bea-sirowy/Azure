import tkinter as tk
from random import choice


class IChingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("I Ching Divination")
        self.question_label = tk.Label(master, text="Think about a question...")
        self.question_label.pack()

        self.throw_button = tk.Button(
            master, text="Throw Coins", command=self.throw_coins
        )
        self.throw_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.read_button = tk.Button(
            master, text="Read Answer", command=self.read_answer, state=tk.DISABLED
        )
        self.read_button.pack()

        self.throws = []

    def throw_coins(self):
        if len(self.throws) < 6:
            result = choice(
                ["6 (---x---)", "7 (---  ---)", "8 (---- ----)", "9 (----o----)"]
            )
            self.throws.append(result)
            self.result_label.config(text="\n".join(self.throws))
            if len(self.throws) == 6:
                self.throw_button.config(state=tk.DISABLED)
                self.read_button.config(state=tk.NORMAL)
        else:
            self.throw_button.config(state=tk.DISABLED)

    def read_answer(self):
        hexagram = "\n".join(self.throws)
        name, interpretation = self.get_hexagram_interpretation(self.throws)
        answer = f"The hexagram you generated is:\n\n{hexagram}\n\nName: {name}\n\nInterpretation: {interpretation}"
        self.result_label.config(text=answer)

    def get_hexagram_interpretation(self, throws):
        # Expanded hexagrams dictionary with all 64 hexagrams
        hexagrams = {
            "111111": (
                "Hexagram 1 - The Creative",
                "Represents strength, creativity, and the drive to bring ideas into reality.",
            ),
            "000000": (
                "Hexagram 2 - The Receptive",
                "Symbolizes receptivity, yielding, and the nurturing aspect of nature.",
            ),
            "100010": (
                "Hexagram 3 - Difficulty at the Beginning",
                "Signifies initial struggle and the importance of perseverance.",
            ),
            "010001": (
                "Hexagram 4 - Youthful Folly",
                "Represents inexperience and the need for guidance.",
            ),
            "111010": (
                "Hexagram 5 - Waiting (Nourishment)",
                "Patience in the face of obstacles, knowing that perseverance will bring success.",
            ),
            "010111": (
                "Hexagram 6 - Conflict",
                "Conflict and disputes can be resolved through persistence and adherence to the truth.",
            ),
            "010000": (
                "Hexagram 7 - The Army",
                "Discipline and leadership are essential for achieving victory.",
            ),
            "000010": (
                "Hexagram 8 - Holding Together (Union)",
                "Unity and cooperation are vital for success.",
            ),
            "111011": (
                "Hexagram 9 - The Taming Power of the Small",
                "Small forces can achieve significant outcomes through gentle persistence.",
            ),
            "110111": (
                "Hexagram 10 - Treading (Conduct)",
                "Caution and mindfulness are required to navigate potential dangers.",
            ),
            "111000": (
                "Hexagram 11 - Peace",
                "Harmony and prosperity through balanced and integrated actions.",
            ),
            "000111": (
                "Hexagram 12 - Standstill (Stagnation)",
                "Stagnation and obstacles; patience and inner strength are needed.",
            ),
            "101111": (
                "Hexagram 13 - Fellowship with Men",
                "Building relationships and fostering community.",
            ),
            "111101": (
                "Hexagram 14 - Possession in Great Measure",
                "Abundance and wealth attained through wisdom and integrity.",
            ),
            "001000": (
                "Hexagram 15 - Modesty",
                "Humility and modesty lead to success and respect.",
            ),
            "000100": (
                "Hexagram 16 - Enthusiasm",
                "Positive energy and enthusiasm can drive progress.",
            ),
            "100110": (
                "Hexagram 17 - Following",
                "Adaptability and following the right path lead to success.",
            ),
            "011001": (
                "Hexagram 18 - Work on What Has Been Spoiled",
                "Correcting past mistakes and addressing unresolved issues.",
            ),
            "110000": (
                "Hexagram 19 - Approach",
                "Opportunities are arising; preparation is key.",
            ),
            "000011": (
                "Hexagram 20 - Contemplation (View)",
                "Introspection and observation provide clarity and understanding.",
            ),
            "100101": (
                "Hexagram 21 - Biting Through",
                "Resolving problems with decisiveness and clarity.",
            ),
            "101001": (
                "Hexagram 22 - Grace",
                "Beauty and elegance enhance the substance of actions.",
            ),
            "000001": (
                "Hexagram 23 - Splitting Apart",
                "Periods of decline and disintegration; caution is needed.",
            ),
            "100000": (
                "Hexagram 24 - Return (The Turning Point)",
                "A time of renewal and return to the right path.",
            ),
            "100111": (
                "Hexagram 25 - Innocence (The Unexpected)",
                "Maintaining purity and sincerity brings favorable outcomes.",
            ),
            "111001": (
                "Hexagram 26 - The Taming Power of the Great",
                "Strength restrained and used wisely leads to success.",
            ),
            "100001": (
                "Hexagram 27 - Corners of the Mouth (Providing Nourishment)",
                "Nourishment and care for oneself and others.",
            ),
            "011110": (
                "Hexagram 28 - Preponderance of the Great",
                "Great pressure and challenges require resilience.",
            ),
            "010010": (
                "Hexagram 29 - The Abysmal (Water)",
                "Enduring danger and hardship through perseverance.",
            ),
            "101010": (
                "Hexagram 30 - The Clinging (Fire)",
                "Clarity and awareness in the midst of complexity.",
            ),
            "001110": (
                "Hexagram 31 - Influence (Wooing)",
                "Mutual attraction and influence lead to positive outcomes.",
            ),
            "011100": (
                "Hexagram 32 - Duration",
                "Consistency and perseverance ensure long-term success.",
            ),
            "001111": (
                "Hexagram 33 - Retreat",
                "Strategic withdrawal to avoid unfavorable situations.",
            ),
            "111100": (
                "Hexagram 34 - The Power of the Great",
                "Great power used wisely and with restraint.",
            ),
            "000101": (
                "Hexagram 35 - Progress",
                "Gradual and steady progress through diligence.",
            ),
            "101000": (
                "Hexagram 36 - Darkening of the Light",
                "Maintaining inner light and strength in difficult times.",
            ),
            "101011": (
                "Hexagram 37 - The Family",
                "Harmony and structure within family and community.",
            ),
            "110101": (
                "Hexagram 38 - Opposition",
                "Accepting differences and finding common ground.",
            ),
            "001010": (
                "Hexagram 39 - Obstruction",
                "Overcoming obstacles through perseverance and creativity.",
            ),
            "010100": (
                "Hexagram 40 - Deliverance",
                "Relief from difficulties through decisive action.",
            ),
            "110001": (
                "Hexagram 41 - Decrease",
                "Voluntary sacrifice and reducing excess lead to gains.",
            ),
            "100011": (
                "Hexagram 42 - Increase",
                "Growth and progress through generosity and effort.",
            ),
            "111110": (
                "Hexagram 43 - Breakthrough",
                "Resolute action leads to significant change.",
            ),
            "011111": (
                "Hexagram 44 - Coming to Meet",
                "Unexpected encounters that require careful handling.",
            ),
            "000110": (
                "Hexagram 45 - Gathering Together (Massing)",
                "Unity and collective effort achieve great results.",
            ),
            "011000": (
                "Hexagram 46 - Pushing Upward",
                "Steady growth and progress through perseverance.",
            ),
            "010011": (
                "Hexagram 47 - Oppression (Exhaustion)",
                "Facing adversity with strength and resilience.",
            ),
            "110010": ("Hexagram 48 - The Well", "Source of nourishment and wisdom."),
            "101110": (
                "Hexagram 49 - Revolution (Molting)",
                "Transformation and change through reform.",
            ),
            "011101": (
                "Hexagram 50 - The Cauldron",
                "Nurturing and sustaining creative forces.",
            ),
            "001011": (
                "Hexagram 51 - The Arousing (Shock, Thunder)",
                "Sudden shock that awakens and motivates.",
            ),
            "110100": (
                "Hexagram 52 - Keeping Still (Mountain)",
                "Stillness and introspection bring clarity.",
            ),
            "001101": (
                "Hexagram 53 - Development (Gradual Progress)",
                "Steady progress through patience and diligence.",
            ),
            "101100": (
                "Hexagram 54 - The Marrying Maiden",
                "Adaptability and finding one's place within constraints.",
            ),
            "001001": (
                "Hexagram 55 - Abundance (Fullness)",
                "Abundance and success through wise management.",
            ),
            "011011": (
                "Hexagram 56 - The Wanderer",
                "Navigating through changing circumstances with flexibility.",
            ),
            "101101": (
                "Hexagram 57 - The Gentle (Penetrating, Wind)",
                "Gentle and persistent efforts lead to success.",
            ),
            "011110": (
                "Hexagram 58 - The Joyous (Lake)",
                "Joy and openness foster positive interactions.",
            ),
            "010110": (
                "Hexagram 59 - Dispersion (Dissolution)",
                "Resolving tensions and fostering unity.",
            ),
            "001100": (
                "Hexagram 60 - Limitation",
                "Embracing constraints to achieve clarity and focus.",
            ),
            "110110": (
                "Hexagram 61 - Inner Truth",
                "Sincerity and integrity lead to understanding and harmony.",
            ),
            "000011": (
                "Hexagram 62 - Preponderance of the Small",
                "Attention to detail and small actions bring success.",
            ),
            "011111": (
                "Hexagram 63 - After Completion",
                "Completion and the need to maintain progress.",
            ),
            "100011": (
                "Hexagram 64 - Before Completion",
                "Signifies approaching the final stages of a task, urging caution and careful execution.",
            ),
        }
        # Example simple way to convert throws to hexagram code
        hex_code = "".join(["1" if "7" in t or "9" in t else "0" for t in throws])
        return hexagrams.get(
            hex_code,
            (
                "Unknown Hexagram",
                "The interpretation for this combination is not available.",
            ),
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = IChingApp(root)
    root.mainloop()
