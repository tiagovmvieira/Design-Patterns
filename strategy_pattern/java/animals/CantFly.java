package strategy_pattern.java.animals;

public class CantFly implements Flys {

    @Override
    public String fly() {
        
        return "I can't fly";
        
    }

}
