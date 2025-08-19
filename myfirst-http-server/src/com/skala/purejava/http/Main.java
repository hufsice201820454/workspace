package com.skala.purejava.http;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.skala.purejava.http.model.User;
import com.skala.purejava.http.repo.FileUserRepository;
import com.skala.purejava.http.repo.UserRepository;
import com.skala.purejava.http.util.JsonUtil;
import com.skala.purejava.http.repo.FileUserRepository;
import com.skala.purejava.http.repo.UserRepository;
import com.skala.purejava.http.server.*;

import java.nio.file.Path;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        //int port = 8080, threads = 16;
        // Path dataFile = Path.of("data", "users.json");

        // // 1. Repository 생성 (파일 없으면 자동으로 [] 초기화됨)
        // UserRepository repo = new FileUserRepository(dataFile);

        // // 2. 코드에서 직접 User 객체 생성
        // User u1 = new User(null, "홍길동", "hong@example.com", Arrays.asList("검술", "전략"));
        // User u2 = new User(null, "임꺽정", "lim@example.com", List.of("산적질", "도술"));

        // // 3. 저장 (id 자동 할당)
        // repo.create(u1);
        // repo.create(u2);

        // // 4. 전체 조회
        // var allUsers = repo.findAll();

        // // 5. JSON 직렬화
        // ObjectMapper mapper = JsonUtil.mapper();
        // String json = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(allUsers);

        // // 6. 화면 출력
        // System.out.println("=== 현재 저장된 사용자 목록 ===");
        // System.out.println(json);
        int port = 8080;
        int threads = 16;

        // 파일 저장소 준비 (부팅 시 파일→Map 로드 포함)
        Path dataFile = Path.of("data", "users.json");
        UserRepository repo = new FileUserRepository(dataFile);

        // 라우팅 내장 서버 생성 및 시작 (Socket 기반)
        HttpUserHandler server = new HttpUserHandler(port, threads, repo);
        System.out.println("SKALA 2 First HTTP Server (socket) at http://localhost:" + port);
        server.start(); // 블로킹
    }
}
