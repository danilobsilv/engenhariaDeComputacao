    /*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import view.Agendamento;
import view.Destinos;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.io.BufferedReader;
import javax.swing.DefaultListModel;

/**
 *
 * @author PauloR
 */
public class Destinos_Controller {
    private final Destinos view;
    
    public Destinos_Controller(Destinos view){
        this.view = view;
    }
    
    public void goAgendamentoScreen(){
        Agendamento agendamento = new Agendamento();
        agendamento.setVisible(true);
        this.view.dispose();
    }

    public void lerDestinos(DefaultListModel mod){
        ArrayList<String> destinos = new ArrayList<>();
        try{
            FileReader fr = new FileReader("sistema_venda_bilhetes_naval/funcionarioSenha.txt");
            BufferedReader ler = new BufferedReader(fr);
            while (ler.ready()){
                String linha = ler.readLine();
            
                destinos.add(linha);
            ler.close();
            fr.close();
        }
    }
        catch (IOException error){
            error.printStackTrace();
        }
    }
    
    
    
    
}
