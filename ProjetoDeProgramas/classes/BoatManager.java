package classes;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class BoatManager {
    private String boat;


    public String getBoat() {
        return boat;
    }

    public void setBoat(String boat) {
        this.boat = boat;
    }

    public void cadastrarBarco(String boat) {
        try{
            FileWriter fw = new FileWriter("barcoscadastrados.txt", true);
            BufferedWriter escritor = new BufferedWriter(fw);
            
            escritor.write(boat);
            escritor.newLine();
            escritor.close();
        }     
        catch (IOException error){
            error.printStackTrace();
        }   
    }

    public void alterarBarco() {

    }

    public void excluirBarco() {

    }    




}
