import { FC, useState } from 'react';
import {
  NavIdProps,
  Panel,
  PanelHeader,
  PanelHeaderBack,
  Div,
  Avatar,
  Group,
  Text,
  Button,
  Cell,
} from '@vkontakte/vkui';
import { useRouteNavigator } from '@vkontakte/vk-mini-apps-router';
import LogoImage from '../assets/logo.png';
import LeftCompass from '../assets/leftCompass.png';
import RightCompass from '../assets/rightCompass.png';
import Scroll from '../assets/scroll.png';
import API from '../api';

export const Advice: FC<NavIdProps> = ({ id, fetchedUser }) => {
  const routeNavigator = useRouteNavigator();
  const { photo_200, id: userId, first_name, last_name } = { ...fetchedUser };

  const [advice, setAdvice] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const fetchAdvice = async () => {
    setLoading(true);
    setError(null);
    try {
      const api = new API();
      const data = await api.call(userId);
      setAdvice(data.advice);
    } catch (err) {
      setError('Не удалось получить совет. Попробуйте позже.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Panel id={id}>
      <PanelHeader before={<PanelHeaderBack onClick={() => routeNavigator.back()} />}>
        {/* <Text className='panel-header-text'>Совет дня</Text> */}
      </PanelHeader>

      <Group className="group">
        <Div className="div-logo">
          <img width={110} className='LeftCompass' src={LeftCompass} alt="LeftCompass" />
          <img width={230} className="logo-image" src={LogoImage} alt="Logo" />
          <img width={110} className="RightCompass" src={RightCompass} alt="RightCompass" />
        </Div>

        <Div className='div-user'>
          {fetchedUser && (
            <Cell before={photo_200 && <Avatar className="avatar" style={{ width: 150, height: 150 }} src={photo_200} />}>
              <Text className="user-name">{`${first_name} ${last_name}`}</Text>
            </Cell>
          )}
        </Div>


        <div className="div-scroll">
          <div className="image-container">
            <img src={Scroll} alt="Scroll" width={500} height={350} className="scroll-image" />
            <div className="overlay-text">
              {loading && <Text>Загрузка совета...</Text>}
              {!loading && error && <Text>{error}</Text>}
              {!loading && !error && advice && <Text>{advice}</Text>}
            </div>
          </div>
        </div>

        <Div className="button-container">
          <Button stretched size="l" className="button" mode="secondary" onClick={fetchAdvice}>
            <Text className="button-text">Получить совет</Text>
          </Button>
        </Div>
      </Group>
    </Panel>
  );
};