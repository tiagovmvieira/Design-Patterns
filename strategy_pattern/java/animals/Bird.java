package strategy_pattern.java.animals;

public class Bird extends Animal {

    public Bird(){

        super();
        setSound("Tweet");

        flyingType = new ItFlys();
        
    }
    
}
