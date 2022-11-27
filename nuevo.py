import matplotlib.pyplot as plt

manzanas = [20,10,25,30]
nombres = ["Ana","Juan","Diana","Catalina"]
plt.pie(manzanas, labels=nombres, autopct="%0.1f %%")
plt.axis("equal")
plt.show()
