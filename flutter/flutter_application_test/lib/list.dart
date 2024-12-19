import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class ResultPage extends StatefulWidget {
  @override
  _ResultPageState createState() => _ResultPageState();
}

class _ResultPageState extends State<ResultPage> {
  List<dynamic> _results = [];

  @override
  void initState() {
    super.initState();
    _fetchResults();
  }

  Future<void> _fetchResults() async {
    final response = await http.get(Uri.parse('http://192.168.117.95:5000/login2'));
    if (response.statusCode == 200) {
      setState(() {
        _results = json.decode(response.body);
      });
    } else {
      // Manejar error
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error al carregar els resultats')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Resultats')),
      body: _results.isEmpty
          ? Center(child: CircularProgressIndicator())
          : ListView.builder(
              itemCount: _results.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(_results[index]['nom']),
                  subtitle: Text(_results[index]['email']),
                );
              },
            ),
    );
  }
}