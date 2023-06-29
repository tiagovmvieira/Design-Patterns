package strategy_pattern.java.demo;

public abstract class Duck{

    FlyBehaviour flyBehaviour;
    QuackBehaviour quackBehaviour;

    public Duck(){

    }

    public abstract void display();

    public void swim(){

        System.out.println("All ducks float, even decoys!");
    }
    
    public void performQuack(){
        
        quackBehaviour.quack();
    }

    public void performFly(){
        
        flyBehaviour.fly();
    }

    public void setFlyBehaviour(FlyBehaviour theFlyBehaviour){

        this.flyBehaviour = theFlyBehaviour;
    }

    public void setQuackBehaviour(QuackBehaviour theQuackBehaviour){

        this.quackBehaviour = theQuackBehaviour;
    }

}