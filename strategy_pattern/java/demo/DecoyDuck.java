package strategy_pattern.java.demo;

public class DecoyDuck extends Duck {

    public DecoyDuck(){

        flyBehaviour = new FlyNoWay();
        quackBehaviour = new MuteQuack();
    }

    @Override
    public void display() {
        
        System.out.println("I'm a decoy duck");
    }
    
}
