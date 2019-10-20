import React, {useState} from 'react';
import { View, TextInput, StyleSheet, Text, Button, TouchableOpacity} from 'react-native';
import Firebase from '../config/firebase'
import Card from '../components/Card'

const Login = props =>  {
    
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    
    const loginHandler = () => {
        Firebase.auth().signInWithEmailAndPassword(email, password).then(()=>{props.navigation.navigate('Main')}).catch(error=>console.log(error));        
    }
        return(
            <View style={styles.container}>
            <Card style={styles.inputContainer}>
            <View>
               <TextInput style={styles.inputBox} placeholder="Email" autoCapitalize='none' onChangeText={(value) => {
                  setEmail(value);
                }}  />
                <TextInput style={styles.inputBox} placeholder="Password" secureTextEntry={true} onChangeText={(value) => {
                  setPassword(value);
                }}  />
                <TouchableOpacity style={styles.button} onPress={loginHandler}  >
                    <Text style={styles.buttonText}>Login</Text>
                </TouchableOpacity>
                <Button title="Not Registered Yet!" onPress={() => {props.navigation.navigate('SignUp')}} />
            </View>
            </Card>
            </View>
        )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 50,
        alignItems: 'center',
        justifyContent: 'center'
    },
    inputContainer: {
        padding: 15,
        width: '90%',
        maxWidth: '100%',
        alignItems: 'center'
      },
    inputBox: {
        margin: 10,
        padding: 15,
        paddingBottom: 0,
        fontSize: 16,
        borderColor: 'rgba(0,0,0,0.05)',
        borderBottomWidth: 1,
        textAlign: 'center'
    },
    button: {
        marginTop: 30,
        marginBottom: 20,
        paddingVertical: 5,
        alignItems: 'center',
        backgroundColor: '#006400',
        borderColor: '#006400',
        borderWidth: 1,
        borderRadius: 5,
        width: 200
    },
    buttonText: {
        fontSize: 20,
        fontWeight: 'bold',
        color: '#fff'
    },
    buttonSignup: {
        fontSize: 12
    }
});

export default Login;