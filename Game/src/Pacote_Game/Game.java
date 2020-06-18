package Pacote_Game;
import java.awt.Graphics2D;
import java.awt.Image;
import javax.swing.JFrame;
import javax.swing.Timer;
public class Game extends JFrame {
    public static void main(String Args[]){
        new Game();
    }
    public Game(){
        componentes();
    }
    public void componentes(){
        //Título da tela
        setTitle("ThinkTitleLater");
        //Permite encerrar a aplicação
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //Define o tamanho da tela
        setSize(800,600);
        //Coloca a janela no centro da tela
        setLocationRelativeTo(null);
        //Não pode ser redimensionado
        setResizable(false);
        //Torna visível a tela
        setVisible(true);
        
    }
    private Timer timer;
    private Fase fase;
    private Image fundo;
    private Graphics2D grafico;
    
}