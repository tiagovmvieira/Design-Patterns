package strategy_pattern.java.demo;

public class RedheadDuck extends Duck{

    public RedheadDuck(){

        flyBehaviour = new FlyNoWay();
        quackBehaviour = new Quack();
    }

    @Override
    public void display() {
        
        System.out.println("I'm a Redhead duck");
    }
    
}
