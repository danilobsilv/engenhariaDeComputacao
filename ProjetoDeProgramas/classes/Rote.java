package classes;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Rote {
    private String origem;
    private String destino;
    
    public Rote(String origem, String destino) {
        this.origem = origem;
        this.destino = destino;
    }

    public String getOrigem() {
        return origem;
    }

    public void setOrigem(String origem) {
        this.origem = origem;
    }

    public String getDestino() {
        return destino;
    }

    public void setDestino(String destino) {
        this.destino = destino;
    }

    public void serializeRote(ArrayList<Rote> roteArrayList, String nomeArquivo){
        File arquivo = new File(nomeArquivo);
        try{
            arquivo.delete();
            arquivo.createNewFile();

            ObjectOutputStream objectOutput = new ObjectOutputStream(new FileOutputStream(arquivo));
            objectOutput.writeObject(roteArrayList);
            objectOutput.close();
        }
        
        catch(IOException err){
            err.printStackTrace();
        }
    }
    
    public ArrayList<Rote> readBinaryRote(String nomeArquivo){
        ArrayList<Rote> listRote = new ArrayList<>();
        
        try{
            File arquivo = new File(nomeArquivo);
            if (arquivo.exists()){
                ObjectInputStream objectInput = new ObjectInputStream(new FileInputStream(arquivo));
                listRote = (ArrayList<Rote>)objectInput.readObject();
                objectInput.close();
            }
        }
        catch(IOException err){
            err.printStackTrace(); 
        }
        catch(ClassNotFoundException err){
            err.printStackTrace();
        }
        return (listRote); 

    }
    
}