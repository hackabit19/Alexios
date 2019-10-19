import React from 'react';
import { View, TextInput, StyleSheet, Text, Button, TouchableOpacity} from 'react-native';
import Firebase from '../config/firebase'


class Login extends React.Component{
    
    state = {
        email: '',
        password: ''
    }
    
    loginHandler = () => {
        const {email, password} = this.state;
        Firebase.auth().signInWithEmailAndPassword(email, password).then(()=>{this.props.navigation.navigate('Main')}).catch(error=>console.log(error));        
    }
    
    render(){
        return(
            <View style={styles.container}>
                <TextInput value={this.state.email} onChangeText={email => this.setState({email})} placeholder='Email' autoCapitalize='none' />
                <TextInput value={this.state.password} onChangeText={password => this.setState({password})} placeholder="Password" secureTextEntry={true}/>
                <Button title="Login" onPress={()=>{this.loginHandler}} />
                <TouchableOpacity onPress={() => {this.props.navigation.navigate('SignUp')}}>
                    <Text>Not Signed up yet</Text>
                </TouchableOpacity>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
});

export default Login;