package classes;

public class Boat {
    private String name;
    private String capacity;

    public Boat(String name, String capacity) {
        this.name = name;
        this.capacity = capacity;
    }

    public Boat(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }
    
}
