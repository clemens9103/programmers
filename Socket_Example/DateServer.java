import java.net.*;
import java.io.*;
import java.util.Date;

public class DateServer {
    public static void main(String[] args) {
        int port = 6013; // 서버가 사용할 포트 번호
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("DateServer is running on port " + port);

            while (true) {
                try (Socket clientSocket = serverSocket.accept()) {
                    PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                    // 현재 날짜 및 시간을 클라이언트에게 보냅니다.
                    out.println(new Date().toString());
                } catch (IOException e) {
                    System.err.println("Error handling client: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.err.println("Could not listen on port " + port + ": " + e.getMessage());
        }
    }
}