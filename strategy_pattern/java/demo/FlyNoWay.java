package strategy_pattern.java.demo;

public class FlyNoWay implements FlyBehaviour {

    @Override
    public void fly() {
        
        System.out.println("I can't fly");
    }
    
}
