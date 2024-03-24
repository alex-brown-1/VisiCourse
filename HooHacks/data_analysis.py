import pandas
import numpy 
import matplotlib.pyplot as plt
import ratemyprofessor
from sklearn.linear_model import LinearRegression
import plotly.express as px

grade_data = (pandas.read_csv("Grade Distribution Final.csv"))

grade_data.dropna(subset=["ratings", "GPA"], inplace=True)

#making linear model
r = grade_data["ratings"].corr(grade_data["GPA"])
x = grade_data[["ratings"]]
y = grade_data["GPA"]

model = LinearRegression()
model.fit(x, y)
m = model.coef_[0]
b = model.intercept_


plt.scatter(grade_data["ratings"], grade_data["GPA"])
plt.plot(x, m*x + b, color="black")
plt.xlabel('Professor Rating')
plt.ylabel('GPA')
plt.title('GPA vs. Professor Rating at Virginia Tech (CS Courses)')
plt.show()

#searching
def filter(courseID):
    
    result = grade_data[grade_data["Course No."] == courseID]
    result = result[result["num_ratings"] > 0]
    result = result[["Instructor", "Course No.", "GPA", "ratings", "difficulties"]]

    if (result.empty): print("CS Course Not Found")
    else:
        fig = px.scatter_3d(result, x='GPA', y='ratings', z='difficulties', opacity=1, color="Course No.", hover_name="Instructor")
        
        return fig.write_html("new_3d-plot.html")