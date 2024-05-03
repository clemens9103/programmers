import java.net.*;
import java.io.*;

public class DateClient {
    public static void main(String[] args) {
        String hostname = "localhost"; // 서버의 호스트명 또는 IP 주소
        int port = 6013; // 서버의 포트 번호

        try (Socket socket = new Socket(hostname, port)) {
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            // 서버로부터 받은 메시지를 출력합니다.
            System.out.println("Server date: " + in.readLine());
        } catch (UnknownHostException e) {
            System.err.println("Unknown host: " + hostname);
        } catch (IOException e) {
            System.err.println("I/O error: " + e.getMessage());
        }
    }
}
