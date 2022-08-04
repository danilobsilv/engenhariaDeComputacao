package supermercado_pp;

import java.util.ArrayList;

public class Pedido {
    private String nomeCliente;
    private ArrayList<Item> produtosEscolhidos;
    private TiposDePagamento modoPagamento;
    
    public Pedido(String nomeCliente, ArrayList<Item>  produtosEscolhidos, TiposDePagamento modoPagamento) {
        this.nomeCliente = nomeCliente;
        this. produtosEscolhidos =  produtosEscolhidos;
        this.modoPagamento = modoPagamento;
    }

    public String getNomeCliente() {
        return nomeCliente;
    }

    public void setNomeCliente(String nomeCliente) {
        this.nomeCliente = nomeCliente;
    }

    

    public TiposDePagamento getModoPagamento() {
        return modoPagamento;
    }

    public void setModoPagamento(TiposDePagamento modoPagamento) {
        this.modoPagamento = modoPagamento;
    }

   
    public void listarPedidosDoCLiente(Cliente cliente){
        for (Item item : produtosEscolhidos) {
            System.out.printf("Pedidos: --> %s\n",item.getProduto().getNome());      
        }
    }

    public ArrayList<Item> getProdutosEscolhidos() {
        return produtosEscolhidos;
    }

    public void setProdutosEscolhidos(ArrayList<Item> produtosEscolhidos) {
        this.produtosEscolhidos = produtosEscolhidos;
    }   
}
