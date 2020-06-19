package Pacote_Game;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;
public class Game extends JFrame {
    public static void main(String Args[]){
        new Game();
    }
    public Game(){
        componentes();
        inicializar();
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
    public void inicializar(){
        fase = new Fase();
        add(fase);
        ImageIcon referencia = new ImageIcon("SPRITES/background/PNG/Battleground3/Bright/Battleground3.png");
        fundo = referencia.getImage();
         /*Instacia o objeto personagem*/
         personagem = new Personagem();
    }
    private Timer timer;
    private Fase fase;
    private Image fundo;
    private Graphics2D grafico;
    private Personagem personagem;

    private class Listener implements ActionListener{
        public void actionPerfomed(ActionEvent e){
            fase.repaint();
        }

        @Override
        public void actionPerformed(ActionEvent ae) {
            throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
        }
    }
    public class Fase extends JPanel{
       private static final long serialVersionUID = 1l;

       protected static final int altura = 600;
       protected static final int largura = 600;

       protected Fase(){
           setDoubleBuffered(true);
       }
       public void paint(Graphics g){
           grafico = (Graphics2D) g;
           grafico.drawImage(fundo,0,0, null);
           /*Desenha Personagem*/
           grafico.drawImage(personagem.getImagem(), personagem.getX(), personagem.getY(), personagem.getX() + personagem.getLar(), personagem.getY() + personagem.getAlt(), 1+(personagem.getPos() * personagem.getLar()), 1, 1+(personagem.getPos() * personagem.getLar()) + personagem.getLar(), personagem.getAlt() +1,null );
           g.dispose();
       }
       public int getLar(){
           return largura;
       }
       public int getAlt(){
           return altura;
       }
    }
}
