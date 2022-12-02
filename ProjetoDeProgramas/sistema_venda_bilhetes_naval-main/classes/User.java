package classes;

import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.Serializable;

import view.Login;
import classes.MainManager;


public class User implements Serializable{
    private static boolean verificador;
    private static boolean token;
    public  String login;
    public  String senha;
    private Client cliente;

    public User(){
        
    }

    public User(String login, String senha) {
        this.login = login;
        this.senha = senha;
    }

    
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public boolean verificarLoginSenha(Login view){
        try{
            FileInputStream fin = new FileInputStream("sistema_venda_bilhetes_naval/clientesCadastrados.txt");
            ObjectInputStream ois = new ObjectInputStream(fin);
            cliente = (Client) ois.readObject();
            String user_login = view.user_login;
            // System.out.println(cliente.getLogin());
            // System.out.println(cliente.getSenha());
            System.out.println(view.user_login);
            System.out.println(view.user_password);
            if(user_login.equals(cliente.getLogin())  && view.user_password.equals(cliente.getSenha())){
                verificador = true;
            }
            else{
                verificador = false;
            }
            ois.close();
            fin.close();

            
    
            // System.out.println(f1.toString());
            // System.out.println(d1.toString());
            // System.out.println(uea.toString());
        }catch(Exception e){
            // e.printStackTrace();
            System.out.println(1);
        }
        return verificador;
    }

    public boolean verificarUsuarioLogin(){
        try{
            FileReader fw = new FileReader("sistema_venda_bilhetes_naval/funcionarioNome.txt");
            BufferedReader ler = new BufferedReader(fw);

            while (ler.ready()){
                String linha = ler.readLine ();
                if (linha.contains(login)){
                    token = true;
                    break;
                }
                else{
                    token = false;
                }
            }
            ler.close();
            fw.close();
        }
        catch (IOException error){
            error.printStackTrace();
        }
        if (token == true){
            verificador = true;
        }
        else{
            verificador = false;
        }
    return verificador;
    }

    public boolean verificarUsuarioSenha(){
        try{
            FileReader fr = new FileReader("sistema_venda_bilhetes_naval/funcionarioSenha.txt");
            BufferedReader ler = new BufferedReader(fr);
            while (ler.ready()){
                String linha = ler.readLine();
                if (linha.contains(senha)){
                    token = true;
                    break;
                }
                else{
                    token = false;
                }
            }
            ler.close();
            fr.close();
        }
        catch (IOException error){
            error.printStackTrace();
        }
        if (token == true){
            verificador = true; 
        }
        else{
            verificador = false;
        }
        return verificador;
    }
}
