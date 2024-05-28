if self.usuario not in [u['usuario'] for u in self.datos_biblioteca['usuarios']]:
            self.datos_biblioteca['usuarios'].append({'ombre_usuario': self.usuario})
            print('Usuario registrado exitosamente!')