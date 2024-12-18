import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert'; // Importa la biblioteca dart:convert

class LoginPage extends StatelessWidget {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Login')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _usernameController,
              decoration: InputDecoration(labelText: 'Username'),
            ),
            TextField(
              controller: _passwordController,
              decoration: InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                _login(context);
              },
              child: Text('Login'),
            ),
          ],
        ),
      ),
    );
  }

  void _login(BuildContext context) async {
    final username = _usernameController.text;
    final password = _passwordController.text;

    final response = await http.get(
      Uri.parse('http://192.168.117.95:5000/prova'),
    );

    if (response.statusCode == 200) {
      final data = response.body;
      print('Response data: $data');
      Navigator.pushNamed(context, '/list');
    } else {
      print('Failed to load data: ${response.statusCode}');
    }
  }
}