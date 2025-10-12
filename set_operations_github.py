class SkillMatcher:
    def __init__(self, candidate_skills: set, job_requirements: set):
        self.candidate_skills = candidate_skills
        self.job_requirements = job_requirements

    def analyze_skills(self):
        missing = self.job_requirements - self.candidate_skills
        matched = self.candidate_skills & self.job_requirements
        extra = self.candidate_skills - self.job_requirements

        print(f"🟩 Matched Skills: {matched}")
        print(f"🟥 Missing Skills: {missing}")
        print(f"🟨 Extra Skills: {extra}")


def main():
    candidate = {"Python", "SQL", "TensorFlow", "Git"}
    job = {"Python", "SQL", "Machine Learning", "Pandas"}

    matcher = SkillMatcher(candidate, job)
    matcher.analyze_skills()


if __name__ == "__main__":
    main()
