package classes;

import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.ArrayList;


public class MainManager{
    private  ArrayList<Client> clientes = new ArrayList<>();
    public void cadastrarCliente(Client cliente){
        try{
            // FileWriter fw = new FileWriter("sistema_venda_bilhetes_naval/clientesCadastrados.txt", true);
            // BufferedWriter escritor = new BufferedWriter(fw);
            // escritor.writeObject(cliente);
            // escritor.newLine();
            // escritor.close();
            
            FileOutputStream fout = new FileOutputStream("sistema_venda_bilhetes_naval/clientesCadastrados.txt");
            ObjectOutputStream oos = new ObjectOutputStream(fout);
            clientes.add(cliente);
            System.out.println(clientes.size());
            oos.writeObject(clientes);
            // oos.writeChars("\n");
            oos.flush();
            fout.flush();
            oos.close();
            fout.close();

            
        }     
        catch (IOException error){
            error.printStackTrace();
        }   
    }
}
