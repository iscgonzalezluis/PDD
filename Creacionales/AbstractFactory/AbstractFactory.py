

class Pizza

	abstract Pizza crearPizza() #se define un metodo abstracto en la clase pizzeria que sera implementado en cada subclase pizzeria
	
	Pizza(FactoriaIngredientes fi); #se define de este modo por cada subclase dependiendo de la zona, mas que nada por sus proveedores...
		

	Pizza crearPizza() #el creador de pizza es el que instancia la factory concreta, en este caso la de una mexicana 
	{
    		FactoríaIngredientes fi = new IngredientesMexicana();
   		Pizza pizza = new Pizza(fi); // Uso de factory en particular
		pizza.cortar();      //metodo de clase
    		pizza.empaquetar();  //metodo de clase
    		return pizza;
	}