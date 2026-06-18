import json


class RecommendService:

    @staticmethod
    def get_recommendations():

        with open(
            "data/projects.json",
            "r",
            encoding="utf-8"
        ) as f:

            projects = json.load(f)

        projects = sorted(
            projects,
            key=lambda x: x["score"],
            reverse=True
        )

        return projects[:3]