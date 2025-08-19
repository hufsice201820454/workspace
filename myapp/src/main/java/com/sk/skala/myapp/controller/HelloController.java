package com.sk.skala.myapp.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sk.skala.dto.HelloResponse;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class HelloController {

    @GetMapping("/hello")
    // public ResponseEntity<Map<String, String>> hello() {
    //     // Map<String, String> response = new HashMap<>();
    //     // response.put("message", "Helloworld");
    //     // return ResponseEntity.ok(response);
    // }
    public HelloResponse hello(){
        HelloResponse response = new HelloResponse();
        response.setMessage("Hello SpringBoot Response");
        return response;
    }
}
