import React from 'react';
import { View, TextInput, StyleSheet, Text, Button} from 'react-native';

import Firebase from '../config/firebase'
import ImgPicker from '../components/ImgPicker'

class SignUp extends React.Component{
    
    state = {
        name: '',
        carname: '',
        license: '',
        email: '',
        password: ''
    }

    saveImage = (image) => {
       
    }

    signUphandler = () => {
      const {email, password} = this.state;
      Firebase.auth().createUserWithEmailAndPassword(email, password).then(()=>{this.props.navigation.navigate('Main')}).catch(error => console.log(error))}
    
    render(){
        return(
            <View style={styles.container}>
                <TextInput value={this.state.name} onChangeText={name=>this.setState({ name })} placeholder="Full Name" />
                <TextInput value={this.state.carname} onChangeText={carname => this.setState({ carname })} placeholder='Car Name' placeholder="Car Name" />
                <TextInput value={this.state.license} onChangeText={license => this.setState({ license })} placeholder='License' placeholder="License" />
                <ImgPicker onImageTaken={this.saveImage} />
                <TextInput value={this.state.email} onChangeText={email => this.setState({ email })} placeholder='Email' autoCapitalize='none' />
                <TextInput value={this.state.password} onChangeText={password => this.setState({ password })} secureTextEntry={true} placeholder='Password' />
                
                <Button title="SignUp" onPress={this.signUphandler} />
            </View>
        );
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

export default SignUp;