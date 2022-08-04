package supermercado_pp;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args){
        
        Cliente danilo = new Cliente("Danilo Bruno", "000.000.000-00");
        Cliente pantoja = new Cliente("Pantoja", "123.456.789-00");

        Produto produto1 = new Produto("Banana", 7.50f, 100);
        Produto produto2 = new Produto("Maça", 3.50f, 110);
        Produto produto3 = new Produto("Pepino", 12.50f, 73);
        Produto produto4 = new Produto("Arroz", 6.70f, 147);
        Produto produto5 = new Produto("Feijão", 7.50f, 128);
        
        ArrayList<Item> items = new ArrayList<>();
        
        Item item1= new Item(produto1, 2);
        Item item2 = new Item(produto2, 2);
        Item item3 = new Item(produto3, 2);

        items.add(item1);
        items.add(item2);
        items.add(item3);

        Pedido pedido1 = new Pedido("Danilo", items, TiposDePagamento.cartao);

        pedido1.listarPedidosDoCLiente(danilo);
    }
}
