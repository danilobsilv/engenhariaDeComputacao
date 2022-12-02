package classes;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class RoteManager {
    private String rote;
    

    public String getRote() {
        return rote;
    }

    public void setRote(String rote) {
        this.rote = rote;
    }

    public void cadastrarRota(String rote) {
        try{
            FileWriter fw = new FileWriter("rotascadastradas.txt", true);
            BufferedWriter escritor = new BufferedWriter(fw);
            
            escritor.write(rote);
            escritor.newLine();
            escritor.close();
        }     
        catch (IOException error){
            error.printStackTrace();
        }   
    }



    public void alterarRota() {

    }
    
    public void excluirRota() {
        
    }
}
