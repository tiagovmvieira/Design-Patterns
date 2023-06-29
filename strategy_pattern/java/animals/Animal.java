package strategy_pattern.java.animals;

public class Animal {

    private String name;
    private double height;
    private int weight;
    private String favFood;
    private double speed;
    private String sound;

    // Instead of using an interface in a traditional way
    // we use an instance variable that is a subclass
    // of the Flys interface.

    // Animal doesn't care what flyingType does, it just
    // knows the behavior is available to its subclasses

    // This is known as Composition : Instead of inheriting
    // an ability through inheritance the class is composed
    // with Objects with the right ability

    // Composition allows us to change the capabilities of 
    // objects at run time!

    public Flys flyingType;

    public String getName() { return name; }
    public void setName(String newName){

        this.name = newName;
    }
    
    public double getHeight() { return height; }
    public void setHeight(double newHeight){

        this.height = newHeight;
    }

    public int getWeight() { return weight; }
    public void setWeight(int newWeight){
        
        if (newWeight > 0){

            weight = newWeight;
        } else {

            System.out.println("Weight must be bigger than 0");
        }
    
    }

    public String getFavFood() { return favFood; }
    public void setFavFood(String newFavFood){

        this.favFood = newFavFood;
    }

    public double getSpeed() { return speed; }
    public void setSpeed(double newSpeed){

        this.speed = newSpeed;
    }

    public String getSound() { return sound; }
    public void setSound(String newSound){

        this.sound = newSound;
    }

    // Animal pushed off the responsibility for the flying to flyingType
    public String tryToFly(){

        return flyingType.fly();

    }

    // If we want to be able to change the flyingType dynamically
    // we can use te following method
    public void setFlyingAbility(Flys newFlyType){

        flyingType = newFlyType;
    }
    
}
