class SkillMatcher:
    def __init__(self):
        self.required_skills = {
            "Technical-Skills": ["Python", "Tensorflow", "Pytorch", "Git&Github"],
            "Soft-Skills": ["Hardworking", "Teamwork", "Time-Management"]
        }

    def analyze_skills(self, candidate_skills: dict):
        print("🎯 Starting Skill Evaluation...\n")

        for category, required in self.required_skills.items():
            candidate = set(candidate_skills.get(category, []))
            required_set = set(required)

            matched = candidate & required_set
            missing = required_set - candidate
            extra = candidate - required_set

            print(f"📘 Category: {category}")
            print(f"🟩 Matched Skills: {', '.join(matched) if matched else 'None'}")
            print(f"🟥 Missing Skills: {', '.join(missing) if missing else 'None'}")
            print(f"🟨 Extra Skills: {', '.join(extra) if extra else 'None'}")
            print("-" * 50)


def main():
    skill_hunting = SkillMatcher()
    skill_hunting.analyze_skills({
        "Technical-Skills": ["Python", "Tensorflow", "C#", "Git&Github"],
        "Soft-Skills": ["Hardworking", "Teamwork", "Problem-Solving"]
    })


if __name__ == "__main__":
    main()
