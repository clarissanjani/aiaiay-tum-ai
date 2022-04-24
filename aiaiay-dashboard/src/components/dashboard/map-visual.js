import { Bar } from 'react-chartjs-2';
import { Box, Button, Card, CardContent, CardHeader, Divider, useTheme } from '@mui/material';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import ArrowRightIcon from '@mui/icons-material/ArrowRight';

export const MapVisual = (props) => {
  const theme = useTheme();



  return (
    <Card {...props}>
      <CardHeader
        action={(
          <Button
            endIcon={<ArrowDropDownIcon fontSize="small" />}
            size="small"
          >
            Six months year to date
          </Button>
        )}
        title="Where's the next best renewable site?"
      />
      <Divider />
      <CardContent>
        <Box
          sx={{
            height: 400,
            position: 'relative'
          }}
        >
        <a href="../mapvisual.html">
          <img
            alt="Go to pro"
            src="/static/images/static-map.png"
          />
        </a>
        </Box>
      </CardContent>
                <Box
                  sx={{
                    display: 'flex',
                    mt: 30,
                    mx: 'auto',
                    width: '80px',
                    height: '50px',
                    '& img': {
                      width: '100%'
                    }
                  }}
                >

                </Box>

    </Card>
  );
};
