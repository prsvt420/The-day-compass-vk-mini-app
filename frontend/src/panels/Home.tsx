import { FC } from 'react';
import {
  Panel,
  PanelHeader,
  Text,
  Button,
  Group,
  Div,
  NavIdProps,
} from '@vkontakte/vkui';
import { useRouteNavigator } from '@vkontakte/vk-mini-apps-router';
import LogoImage from '../assets/logo.png';
import LeftCompass from '../assets/leftCompass.png';
import RightCompass from '../assets/rightCompass.png';
import Scroll from '../assets/scroll.png';

export interface HomeProps extends NavIdProps { }

export const Home: FC<HomeProps> = ({ id }) => {
  const routeNavigator = useRouteNavigator();

  return (
    <Panel id={id} className="panel">
      <PanelHeader className='panel-header'>
        {/* <Text className='panel-header-text'>Дневной компас</Text> */}
      </PanelHeader>

      <Group className="group">
        <Div className="div-logo">
          <img width={110} className='LeftCompass' src={LeftCompass} alt="LeftCompass" />
          <img width={230} className="logo-image" src={LogoImage} alt="Logo" />
          <img width={110} className="RightCompass" src={RightCompass} alt="RightCompass" />
        </Div>

        <div className="div-scroll">
          <div className="image-container">
            <img src={Scroll} alt="Scroll" width={500} height={350} className="scroll-image" />
            <div className="overlay-text">Добро пожаловать в "Дневной компас"!  Здесь вы найдете уникальные советы, которые помогут сделать ваш день продуктивным и вдохновляющим.</div>
          </div>
        </div>

        <Div className="button-container">
          <Button stretched size="l" className="button" mode="secondary" onClick={() => routeNavigator.push('advice')}>
            <Text className="button-text">Продолжить</Text>
          </Button>
        </Div>
      </Group>
    </Panel>
  );
};
