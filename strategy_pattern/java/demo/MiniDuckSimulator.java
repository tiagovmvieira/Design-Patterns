package strategy_pattern.java.demo;

public class MiniDuckSimulator {

    public static void main(String[] args){

        Duck mallard = new MallardDuck();
        mallard.display();
        mallard.performQuack();
        mallard.performFly();
        mallard.swim();
        
        System.out.println("\n");

        Duck model = new ModelDuck();
        model.display();
        model.performQuack();
        model.performFly();
        model.setFlyBehaviour(new FlyRocketPowered());
        model.performFly();

        System.out.println("\n");

        Duck redhead = new RedheadDuck();
        redhead.display();
        redhead.performQuack();
        redhead.performFly();

        System.out.println("\n");
        
        Duck rubber = new RubberDuck();
        rubber.display();
        rubber.performQuack();
        rubber.performFly();
        rubber.swim();

    }
    
}
