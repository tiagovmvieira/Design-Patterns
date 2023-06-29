package strategy_pattern.java.demo;

public class MuteQuack implements QuackBehaviour {

    @Override
    public void quack() {
        
        System.out.println("<< Silence >>");
    }
    
}
