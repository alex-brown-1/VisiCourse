import ratemyprofessor
import pandas

grade_data = (pandas.read_csv("Grade Distribution Final.csv"))
virginia_tech = ratemyprofessor.get_school_by_name("Virginia Tech")

ratings = []
difficulties = []
num_ratings = []

# Iterate over each teacher to fetch their rating
for teacher in grade_data["Instructor"]:
    if teacher is not None:
        professor = ratemyprofessor.get_professor_by_school_and_name(virginia_tech, teacher)
        # Assuming the professor object has a 'rating' attribute
        if professor is not None and hasattr(professor, 'rating'):
            ratings.append(professor.rating)
            difficulties.append(professor.difficulty)
            num_ratings.append(professor.num_ratings)
        else:
            ratings.append(professor.rating)
            difficulties.append(None)  # For professors not found or without ratings
            num_ratings.append(None)
            
    else:
        ratings.append(professor.rating)
        difficulties.append(None)
        num_ratings.append(None)

grade_data["ratings"] = ratings
grade_data["difficulties"] = difficulties
grade_data["num_ratings"] = num_ratings
grade_data.to_csv("Grade Distribution Final.csv")
"""


"""
grade_rating2 = []
for i in range(1228):
    if type(grade_data["ratings"][i]) == numpy.float64:
        grade_rating2.append(grade_data["ratings"])

grade_data["ratings2"] = grade_rating2
