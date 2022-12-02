package view;
import java.util.ArrayList;

// import controller.Destinos_Controller;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import javax.swing.DefaultListModel;

public class test {
    public static void main(String[] args) {
        
    try{
        String caminho = "src/sistema_venda_bilhetes_naval/rotascadastradas.txt";
        FileReader fr = new FileReader(caminho);
        BufferedReader ler = new BufferedReader(fr);
        String linha = ler.readLine();
        System.out.println(linha);
        // do{
        //     linha = ler.readLine();
        //     System.out.println(linha);
        // }while (linha != null);
        while (true){
            linha = ler.readLine();
            if(linha == null){
                break;
            }
            // mod.addElement(linha);
            System.out.println(linha);
        }
        ler.close();
        fr.close();
    // }catch(FileNotFoundException e){
    //     System.out.println("arquivo n");
    }catch (IOException error){
        // error.printStackTrace();
        System.out.println("1");
    }
}
}
