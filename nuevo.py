import matplotlib.pyplot as plt

porcentaje = [63.27,36.73]
sexo = ["M","F"]
colores = ["#60D394","#FFD97D"]
plt.pie(porcentaje, labels=sexo, autopct="%0.1f %%", colors=colores)}
plt.axis("equal")
plt.show()
