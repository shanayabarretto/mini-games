/*
Author: Shanaya Barretto
Date: March 30th 2022
Program: Hangman
Future improvements: Add play again option, improve gui
*/
import javax.swing.AbstractAction;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.event.ActionEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class Hangman {
    public static String status;
    public static Integer wrong;
    public static Integer right;
    public static char word[]; 
    public static void main(String[] args) throws Exception {
        // game info
        wrong = 0;
        right = 0;
        status = "unsolved";

        // connect to database
        Connection conn = null;
        String url = "jdbc:sqlite:makesure.db";
        conn = DriverManager.getConnection(url);
        Integer index = getRandomNumber(1, 25);
        Statement stmt = null;
        String query = "SELECT * FROM movies WHERE num=" + index;
        stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);
        word = rs.getString("title").toCharArray();


        // setting up the gui
        JFrame frame = new JFrame();
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel panel = new JPanel();
        frame.add(panel);
        panel.setLayout(null);

        JLabel wrongLabel = new JLabel("Incorrect guesses: 0/6");
        wrongLabel.setBounds(135, 5, 300, 50);
        panel.add(wrongLabel);

        JLabel conclude = new JLabel("");
        conclude.setBounds(110, 120, 300, 50);
        panel.add(conclude);

        JLabel title = new JLabel("Guess the word");
        title.setBounds(25, 5, 300, 50);
        panel.add(title);

        // must be done initially
        char compare[] = new char[word.length];
        char printing[] = new char[word.length*2];
        Integer x = 0;
        for (int c = 0; c < printing.length; c += 2) {
            if (word[x] == ' ')
            {
                compare[x] = ' ';
                printing[c] = ' ';
            }
            else {
                compare[x] = '_';
                printing[c] = '_';
            }
            printing[c+1] = ' ';
            x++;
        }

        String current = String.valueOf(printing);
        JLabel statusLabel = new JLabel("Status: " + current);
        statusLabel.setBounds(40, 30, 300, 70);
        panel.add(statusLabel);

        JTextField userText = new JTextField(1);
        userText.setBounds(200, 100, 30, 25);
        panel.add(userText);

        JButton enterButton = new JButton( new AbstractAction("Guess letter") { 
            @Override
            public void actionPerformed( ActionEvent e ) {
                char guess = userText.getText().charAt(0);
                userText.setText("");

                if (status == "unsolved") {
                    Integer preRight = right;
                    for (int iterate = 0; iterate < word.length; iterate++)
                    {
                        if (guess == word[iterate])
                        {
                            right++;
                            compare[iterate] = word[iterate];
                        }
                    }
                    if (preRight == right)
                    {
                        wrong++;
                    }
                    statusLabel.setText("Status: " + printData(compare));
                    wrongLabel.setText("Incorrect guesses: " + wrong + "/6");
                    if (wrong == 6)
                    {
                        status = "failed";
                        conclude.setText("Failed");
                    }

                    Integer left = 0;
                    for (int tempCount = 0; tempCount < compare.length; tempCount++) {
                        if (compare[tempCount] == '_') {
                            left++;
                        }
                    }
                    if (left == 0) {
                        status = "complete";
                        conclude.setText("Good Job");
                    }
                }
            }
        });
        enterButton.setBounds(30, 100, 120, 25);
        panel.add(enterButton);


        frame.setVisible(true);
    }

    public static String printData(char formatChar[])
    {
        char forPrint[] = new char[formatChar.length*2];
        Integer x = 0;
        for (int c = 0; c < forPrint.length; c += 2) {
            if (formatChar[x] == ' ')
            {
                forPrint[c] = ' ';
            }
            else {
                forPrint[c] = formatChar[x];
            }
            forPrint[c+1] = ' ';
            x++;
        }
        return String.valueOf(forPrint);
    }

    public static int getRandomNumber(int min, int max) {
        return (int) ((Math.random() * (max - min)) + min);
    }
}
